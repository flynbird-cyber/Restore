# Restore

English | [한국어](README_KO.md)

**I need stars to develop better extensions. Please give this repository a star.**

If you give it a star, the god of restoration will protect your system. On the other hand, if you don't, your system may be less likely to be restored.

Of course, I'm joking. Don't forget to give this repository a star.

---

A txt2img gallery restoration extension for AUTOMATIC1111 Stable Diffusion WebUI.

## Demo

Restore 100 saved PNG images, select an image, and continue processing with Hires. fix and ADetailer.

https://github.com/user-attachments/assets/8f29bc15-23d5-4b40-ad38-addeec152114

## 1. Purpose

The txt2img output gallery may be cleared after a WebUI restart, browser closure, or error.

Restore loads saved PNG images and their embedded generation information directly into the existing txt2img output gallery, allowing interrupted work to resume.

## 2. Features

- Batch restoration of up to 2,000 images.
- Direct restoration to the existing txt2img output gallery.
- Restoration of embedded PNG generation information.
- No separate gallery tab required.
- Automatic detection of the default image output directory.
- Recursive scanning of the specified directory and its subdirectories.
- References original PNG files.
- No regeneration, modification, or deletion of original images.
- No additional dependencies required in the supported environment.
- Free to use.

## 3. Installation

1. Open AUTOMATIC1111 WebUI.
2. Select the **Extensions** tab.
3. Select **Install from URL**.
4. Enter `https://github.com/flynbird-cyber/Restore.git` in **URL for extension's git repository**. Leave the other fields blank.
5. Click **Install**.
6. After installation is complete, select the **Installed** tab.
7. Verify that Restore is installed and its checkbox is enabled.
8. Click **Apply and restart UI**. The WebUI restarts automatically.
9. Open the **txt2img** tab and check that **Restore saved txt2img gallery (PNG)** is available.

## 4. Usage

1. Open the **txt2img** tab.
2. Expand **Restore saved txt2img gallery (PNG)**.
3. Check the image directory under **Image directory**.
4. Set the number of images to restore under **Last N images**.
   - Range: 1–2,000
   - Default: 1,000
5. Click **Restore PNGs to txt2img gallery**.
6. Select an image in the restored gallery and continue processing.

## 5. Using the restored gallery

The txt2img output gallery is used not only for viewing images but also for inspecting generation information, transferring images, upscaling, and further image processing.

Select an image in the gallery and click **Upscale selected image (✨)** below the gallery to run Hires. fix on the selected image without repeating the initial image generation pass.

The following guide is intended for users unfamiliar with these functions. It explains why Restore is useful and how existing functions can be used after restoring the gallery.

### 5.1. Basic gallery functions

- Image preview and selection
- Generation parameters
- Send to img2img
- Send to Inpaint
- Send to Extras
- Save
- Save ZIP
- Download
- Open Folder

### 5.2. Hires. fix

- Upscaler
- Hires Prompt
- Hires Negative Prompt
- Hires Checkpoint
- Hires Sampler
- Hires Scheduler
- Denoising Strength
- Upscale by
- Resize Width/Height
- Hires Steps
- LoRA (additional network application)
- Automatic reuse of the original seed

### 5.3. Conditional functions with Hires. fix

| Function | Conditions and settings |
| --- | --- |
| Variation Seed | Applied when a variation seed is recorded in the original image and Variation Strength is greater than zero. |
| Variation Strength | Set the variation strength in the current UI. |
| Seed Resize | Set the seed reference resolution in the current UI. |
| Refiner | Select a refiner model and set the switching point. Set the application stage to Second pass or Both passes. |
| ADetailer | Enable the extension. Set the detection model, correction prompt, and denoising strength. Corrections are applied to detected regions. |
| ControlNet | Enable the extension. Specify a control image, preprocessor, and compatible model. Set the application stage to High res only or Both. |
| FreeU | Enable the extension. Use a compatible model and configure Backbone Scale, Skip Scale, and the applicable step range. |
| Dynamic Prompts | Enable the extension. Enter dynamic syntax or wildcards in the main prompt. Leave Hires Prompt empty or set it to the same text as the main prompt. |

Configure the required functions and parameters, select an image in the restored gallery, and click the **✨ button**.

Additional generation and correction functions use the current WebUI settings.

## 6. Scope of support

The functions listed in Section 5 are provided by AUTOMATIC1111 and the relevant extensions. They are not implemented or controlled by Restore.

This guide explains why Restore is useful and how the gallery can be used after restoration.

The operation of individual functions depends on the versions, settings, models, and compatibility of AUTOMATIC1111 and the relevant extensions. Restore does not guarantee that these functions will work.

Restore does not automatically restore all previous extension settings.

## 7. Compatibility and limitations

- Designed for AUTOMATIC1111 v1.10.x and Gradio 3.41.x.
- Compatibility with other versions has not been verified.
- Supports PNG files containing embedded generation parameters.
- PNG files without generation parameters are excluded.
- Recent images are selected by file modification time.
- Does not recover deleted or unsaved images.
- Does not restore all WebUI settings.
- Does not modify or delete original image files.
- Intended for trusted local users.
- Do not expose this extension to untrusted remote users.

## 8. Issues

Report Restore-specific bugs and feature requests through GitHub Issues.

## 9. Developer

- Developer: FOR_000 (Reddit: u/FOR_000)
- Location: Seoul, Republic of Korea
- Source code: Python, 132 lines

## 10. License

GNU Affero General Public License v3.0 (AGPL-3.0).

Free to use, modify, and redistribute under the terms of the license.

See the [LICENSE](LICENSE) file for details.

Copyright © 2026 FOR_000
