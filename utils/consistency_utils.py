"""
Consistency Utilities for Lab 4 — Self-Consistency Mini-Bench

Provides answer extraction and majority voting for self-consistency experiments.
"""

import re
from collections import Counter


def extract_final_answer(response):
    """
    Extract the final answer from a CoT response.
    Looks for patterns like 'ANSWER: 42', 'The answer is 42', 'Final answer: 42'.

    Returns:
        str: extracted answer (normalized), or None if no answer found.
    """
    response = response.strip()

    # Pattern 1: ANSWER: <value>
    match = re.search(r"ANSWER:\s*(.+?)(?:\n|$)", response, re.IGNORECASE)
    if match:
        return _normalize(match.group(1))

    # Pattern 2: "the answer is <value>"
    match = re.search(r"the answer is\s+(.+?)(?:\.|,|\n|$)", response, re.IGNORECASE)
    if match:
        return _normalize(match.group(1))

    # Pattern 3: "= <value>" at end of a line
    match = re.search(r"=\s*(.+?)(?:\n|$)", response)
    if match:
        return _normalize(match.group(1))

    # Pattern 4: last number in the response
    numbers = re.findall(r"-?\d+(?:\.\d+)?", response)
    if numbers:
        return _normalize(numbers[-1])

    return None


def _normalize(answer_str):
    """Normalize an answer string: strip whitespace, lowercase, remove trailing punctuation."""
    if answer_str is None:
        return None
    answer = answer_str.strip().lower().rstrip(".,;:!?")
    # Try to convert to number for numeric comparison
    try:
        val = float(answer)
        if val == int(val):
            return str(int(val))
        return str(val)
    except ValueError:
        return answer


def majority_vote(answers):
    """
    Return the most common answer via majority voting.

    Args:
        answers: List of answer strings (may include None).

    Returns:
        str: The most common non-None answer, or None if all are None.
    """
    valid = [a for a in answers if a is not None]
    if not valid:
        return None
    counter = Counter(valid)
    return counter.most_common(1)[0][0]


def run_self_consistency(prompt_template, problems, generate_fn,
                         n_samples=5, temperature=0.7):
    """
    Run self-consistency experiment across all problems.

    Args:
        prompt_template: String with {problem} placeholder.
        problems: List of dicts with 'id', 'text', 'correct_answer'.
        generate_fn: Callable(prompt, temperature=...) → str.
        n_samples: Number of samples per problem.
        temperature: Sampling temperature.

    Returns:
        List of result dicts with single and consensus accuracy.
    """
    results = []

    for prob in problems:
        prompt = prompt_template.format(problem=prob["text"])
        responses = []
        for _ in range(n_samples):
            resp = generate_fn(prompt, temperature=temperature)
            answer = extract_final_answer(resp)
            responses.append({"response": resp, "answer": answer})

        all_answers = [r["answer"] for r in responses]
        single_answer = all_answers[0]
        consensus = majority_vote(all_answers)
        correct = str(prob["correct_answer"])

        results.append({
            "problem_id": prob["id"],
            "correct_answer": correct,
            "single_answer": single_answer,
            "single_correct": _normalize(single_answer) == _normalize(correct),
            "all_answers": all_answers,
            "consensus_answer": consensus,
            "consensus_correct": _normalize(consensus) == _normalize(correct),
            "agreement_rate": (all_answers.count(consensus) / len(all_answers)
                               if consensus else 0),
        })

    return results
