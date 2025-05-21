from diffusers import StableDiffusionPipeline
import torch

# Load the model with correct dtype based on GPU/CPU availability
if torch.cuda.is_available():
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16
    ).to("cuda")
else:
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5"
    ).to("cpu")

def generate_image(prompt: str, output_path: str):
    image = pipe(prompt).images[0]
    image.save(output_path)
    return output_path
