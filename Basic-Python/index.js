import Bytez from "bytez.js"

const key = "84054bfdf8935293178ba99cbdb362a3"
const sdk = new Bytez(key)

// choose whisper-large-v3
const model = sdk.model("openai/whisper-large-v3")

// send input to model
const { error, output } = await model.run("https://huggingface.co/datasets/huggingfacejs/tasks/resolve/main/audio-classification/audio.wav")

console.log({ error, output });