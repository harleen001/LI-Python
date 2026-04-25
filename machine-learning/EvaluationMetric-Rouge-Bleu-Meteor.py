# ROUGE Score (no LLM loaded, using pre-defined lists of texts as LLM outputs (predictions) and references)
import evaluate
rouge_metric = evaluate.load('rouge')
rouge_results = rouge_metric.compute(
    predictions=predictions,
    references=references
)
print("ROUGE Scores:", rouge_results)

# BLEU Score (no LLM loaded, using pre-defined lists of texts as LLM outputs (predictions) and references)
bleu_metric = evaluate.load("bleu")
bleu_results = bleu_metric.compute(
    predictions=predictions,
    references=references
)
print("BLEU Score:", bleu_results)

# METEOR (requires references to be a list of lists)
meteor_metric = evaluate.load("meteor")
meteor_results = meteor_metric.compute(
    predictions=predictions,
    references=[[ref] for ref in references]
)
print("METEOR Score:", meteor_results)