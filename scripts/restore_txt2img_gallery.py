"""Restore saved AUTOMATIC1111 txt2img PNGs to its output gallery.

Designed for A1111 v1.10.x / Gradio 3.41.x. No original PNGs are modified.
UI is registered via an always-visible Script under txt2img settings.
"""
import html
import json
from pathlib import Path

import gradio as gr
from PIL import Image

from modules import scripts, shared
from modules.infotext_utils import parse_generation_parameters


def _int(value, default=-1):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def restore_gallery(folder, count):
    try:
        root = Path((folder or '').strip().strip('"')).expanduser().resolve()
        if not root.is_dir():
            return gr.update(), gr.update(), gr.update(), f'Folder not found: {root}'
        paths = [p for p in root.rglob('*.png') if p.is_file()]
        paths.extend(p for p in root.rglob('*.PNG') if p.is_file())
        paths = sorted(set(paths), key=lambda p: (p.stat().st_mtime, str(p)))
        paths = paths[-max(1, _int(count, 1000)):]
    except (OSError, ValueError) as exc:
        return gr.update(), gr.update(), gr.update(), f'Could not scan folder: {exc}'

    gallery, infotexts, prompts, negatives, seeds, subseeds = [], [], [], [], [], []
    first = None
    first_size = None
    for path in paths:
        try:
            with Image.open(path) as pic:
                infotext = pic.info.get('parameters', '')
                size = pic.size
            if not infotext:
                continue
            params = parse_generation_parameters(infotext, [])
            # A1111 patched Gradio will register this real, saved PNG path
            # rather than duplicating pixels in memory.
            pointer = Image.new('RGB', (1, 1))
            pointer.already_saved_as = str(path.resolve())
            gallery.append(pointer)
            infotexts.append(infotext)
            prompts.append(params.get('Prompt', ''))
            negatives.append(params.get('Negative prompt', ''))
            seeds.append(_int(params.get('Seed')))
            subseeds.append(_int(params.get('Variation seed')))
            if first is None:
                first, first_size = params, size
        except (OSError, ValueError, KeyError):
            continue

    if not gallery:
        return gr.update(), gr.update(), gr.update(), 'No saved PNGs with generation metadata found.'

    info = {
        'prompt': prompts[0], 'all_prompts': prompts,
        'negative_prompt': negatives[0], 'all_negative_prompts': negatives,
        'seed': seeds[0], 'all_seeds': seeds,
        'subseed': subseeds[0], 'all_subseeds': subseeds,
        'subseed_strength': 0, 'width': first_size[0], 'height': first_size[1],
        'sampler_name': first.get('Sampler', ''),
        'cfg_scale': first.get('CFG scale', 7),
        'steps': _int(first.get('Steps'), 20),
        'batch_size': 1, 'restore_faces': False, 'face_restoration_model': None,
        'sd_model_name': first.get('Model', ''),
        'sd_model_hash': first.get('Model hash', ''),
        'sd_vae_name': None, 'sd_vae_hash': first.get('VAE hash', ''),
        'seed_resize_from_w': 0, 'seed_resize_from_h': 0,
        'denoising_strength': 0, 'extra_generation_params': {},
        'index_of_first_image': 0, 'infotexts': infotexts,
        'styles': [], 'job_timestamp': '', 'clip_skip': 1,
        'is_using_inpainting_conditioning': False, 'version': None,
    }
    first_html = '<p>' + '<br>\n'.join(html.escape(line) for line in infotexts[0].split('\n')) + '</p>'
    return gallery, json.dumps(info, ensure_ascii=False), first_html, f'Loaded {len(gallery)} images. Select one in txt2img gallery and click ✨.'


class RestoreSavedTxt2imgGallery(scripts.Script):
    def title(self):
        return 'Restore saved txt2img gallery (PNG)'

    def show(self, is_img2img):
        return scripts.AlwaysVisible if not is_img2img else False

    def ui(self, is_img2img):
        if is_img2img:
            return []
        with gr.Accordion('Restore saved txt2img gallery (PNG)', open=False):
            output = shared.opts.outdir_samples or shared.opts.outdir_txt2img_samples or 'outputs/txt2img-images'
            self.folder = gr.Textbox(label='Image directory', value=str(Path(output).resolve()))
            self.count = gr.Slider(label='Last N images', minimum=1, maximum=2000, value=1000, step=1)
            self.restore = gr.Button('Restore PNGs to txt2img gallery')
            self.status = gr.Textbox(label='Restore status', interactive=False)
        self.gallery = None
        self.geninfo = None
        self.infohtml = None
        self.connected = False
        print('[restore_txt2img_gallery] Settings panel registered')
        return []

    def after_component(self, component, **kwargs):
        elem_id = getattr(component, 'elem_id', None)
        if elem_id == 'txt2img_gallery':
            self.gallery = component
        elif elem_id == 'generation_info_txt2img':
            self.geninfo = component
        elif elem_id == 'html_info_txt2img':
            self.infohtml = component
        if (not getattr(self, 'connected', False)
                and getattr(self, 'restore', None) is not None
                and getattr(self, 'gallery', None) is not None
                and getattr(self, 'geninfo', None) is not None
                and getattr(self, 'infohtml', None) is not None):
            self.restore.click(
                fn=restore_gallery,
                inputs=[self.folder, self.count],
                outputs=[self.gallery, self.geninfo, self.infohtml, self.status],
                show_progress=False,
            )
            self.connected = True
            print('[restore_txt2img_gallery] Gallery button connected')
