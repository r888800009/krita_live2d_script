# krita_live2d_script

## **Backup your work before using this script.**

## Description
using this script in Krita to split LR and merge down the layers for Live2D/inochi2d/nijigenerate model development.
it is inspired by [@seagetch](https://github.com/seagetch)'s [gimp-vtuber-scripts](https://github.com/Inochi2D/gimp-vtuber-scripts)

Usecase like this:
- split left and right eye are on the same layer
- multiple layers for rendering the face or body

you can easily rename your layers with the suffix like:
- `_Draft` for the draft layers, it will remove from your final .kra file
- `_LR` for the left and right layers, it will split into two layers with the suffix `_L` and `_R`
- `_MergeDown` for the layers you want to merge down
- `_Flatten` for layer with the filter, it will flatten the layer

for example:
- `eye_LR` will split into `eye_L` and `eye_R` and remove original layer
- `sketch_draft` will remove from the final .kra file
- `face_MergeDown` will merge down the layers below it

also you can modify the script to fit your own usecase. `*_keyword` you can costomize suffix in the script.

when the script done, pop up save as dialog, you can save the file as a new one or overwrite the original file. (we recommend you to save as a new file)

feel free to open an issue if you have any questions or suggestions.

## Related works
you may also interested in the following works:

- [retorillo/live2d-utils: Set of Photoshop JavaScript script for Live2D model development](https://github.com/retorillo/live2d-utils)
- [Meptl/krita-live2d-prep](https://github.com/Meptl/krita-live2d-prep)
- [Inochi2D/gimp-vtuber-scripts: Scripts for automating the process of preparing vtuber models with the GNU Image Manipulation Program](https://github.com/Inochi2D/gimp-vtuber-scripts/tree/main)