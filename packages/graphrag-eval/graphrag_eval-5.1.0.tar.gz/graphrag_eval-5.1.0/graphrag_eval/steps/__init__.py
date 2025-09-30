import json
from collections import defaultdict

from .retrieval_context_ids import recall_at_k
from .sparql import compare_sparql_results


def compare_steps_outputs(reference: dict, actual: dict) -> float:
    ref_output = reference.get("output")
    act_output = actual["output"]
    assert ref_output, "Reference step output is mandatory"
    if reference.get("output_media_type") == "application/sparql-results+json":
        return compare_sparql_results(
            json.loads(ref_output),
            json.loads(act_output),
            reference["required_columns"],
            reference.get("ordered", False),
        )
    if reference.get("output_media_type") == "application/json":
        return float(json.loads(ref_output) == json.loads(act_output))
    if reference["name"] == actual["name"] == "retrieval":
        ref_contexts_ids = [c["id"] for c in json.loads(ref_output)]
        act_contexts_ids = [c["id"] for c in json.loads(act_output)]
        k = actual["args"]["k"]
        return recall_at_k(ref_contexts_ids, act_contexts_ids, k)
    return float(ref_output == act_output)


def match_group_by_output(
        reference_steps: list[list[dict]],
        group_idx: int,
        actual_steps: list[dict],
        candidates_by_name: dict[str, list[int]],
) -> list[tuple[int, int, int, float]]:
    used_actual_indices = set()
    matches = []

    reference_group = reference_steps[group_idx]
    for reference_idx, reference_step in enumerate(reference_group):
        name = reference_step["name"]
        candidates = reversed(candidates_by_name.get(name, []))
        for actual_idx in candidates:
            if actual_idx in used_actual_indices:
                continue
            actual_step = actual_steps[actual_idx]
            score = compare_steps_outputs(reference_step, actual_step)
            if score > 0.0:
                matches.append((group_idx, reference_idx, actual_idx, score))
                used_actual_indices.add(actual_idx)
                break
    return matches


def collect_possible_matches_by_name_and_status(
        group: list[dict],
        actual_steps: list[dict],
        search_upto: int,
) -> dict[str, list[int]]:
    group_by_name = defaultdict(list)

    for j in range(search_upto):
        name = actual_steps[j]["name"]
        if actual_steps[j]["status"] == "success":
            group_by_name[name].append(j)

    reference_names = {item["name"] for item in group}
    return {name: group_by_name[name] for name in reference_names if name in group_by_name}


def get_steps_matches(
        reference_steps: list[list[dict]],
        actual_steps: list[dict],
) -> list[tuple[int, int, int, float]]:
    # when we have autocomplete
    # matches = []
    # search_upto = len(actual_steps)
    # for group_idx in reversed(range(len(reference_steps))):
    #     group = reference_steps[group_idx]
    #     candidates = collect_possible_matches_by_name(group, actual_steps, search_upto)
    #
    #     matched = match_group_by_output(reference_steps, group_idx, actual_steps, candidates)
    #     if len(matched) == len(group):
    #         # update search_upto to just before the highest matched actual index
    #         matches.extend(matched)
    #         search_upto = min(j for (_, j) in matched)
    #     elif len(matched) < len(group):
    #         matches.extend(matched)
    #         break # a step is not matched and missing, abort
    #     else:
    #         break  # a step is not matched and missing, abort
    # return matches

    # for now, we have only the last step(s)
    last_group = reference_steps[-1]
    candidates = collect_possible_matches_by_name_and_status(last_group, actual_steps, len(actual_steps))
    return match_group_by_output(reference_steps, -1, actual_steps, candidates)


def evaluate_steps(
    reference_steps_groups: list[list[dict]],
    actual_steps: list[dict],
    matches: list[tuple[int, int, int, float]] | None = None
) -> float:
    if matches is None:
        matches = get_steps_matches(reference_steps_groups, actual_steps)
    matches_by_group = defaultdict(list)
    scores_by_group = defaultdict(float)
    for ref_group_idx, ref_match_idx, actual_idx, score in matches:
        matches_by_group[ref_group_idx].append(ref_match_idx)
        scores_by_group[ref_group_idx] += score
        reference_steps_groups[ref_group_idx][ref_match_idx]["matches"] \
            = actual_steps[actual_idx]["id"]
    group_ix = -1  # For now, consider only the last reference group of steps
    return scores_by_group[group_ix] / len(reference_steps_groups[group_ix])


def get_steps_evaluation_result_dict(reference: dict, target: dict) -> dict:
    eval_result = {}
    act_steps = target.get("actual_steps", [])
    eval_result["actual_steps"] = act_steps
    for act_step in act_steps:
        if act_step["name"] == "retrieval":
            from .retrieval_answer import get_retrieval_evaluation_dict
            result = get_retrieval_evaluation_dict(
                question_text=reference["question_text"],
                reference_answer=reference.get("reference_answer"),
                actual_answer=target.get("actual_answer"),
                actual_contexts=json.loads(act_step["output"])
            )
            act_step.update(result)
    if "reference_steps" in reference:
        ref_steps = reference["reference_steps"]
        matches = get_steps_matches(ref_steps, act_steps)
        steps_score = evaluate_steps(ref_steps, act_steps, matches)
        eval_result["steps_score"] = steps_score
        for ref_group_idx, ref_match_idx, act_idx, _ in matches:
            ref_step = ref_steps[ref_group_idx][ref_match_idx]
            act_step = act_steps[act_idx]
            if ref_step["name"] == "retrieval":
                from .retrieval_context_texts import \
                    get_retrieval_evaluation_dict
                res = get_retrieval_evaluation_dict(
                    reference_contexts=json.loads(ref_step["output"]),
                    actual_contexts=json.loads(act_step["output"])
                )
                act_step.update(res)
    return eval_result
