# 3D Texture Inference

This repository is a forked repository from "[PIFu: Pixel-Aligned Implicit Function for High-Resolution Clothed Human Digitization](https://arxiv.org/abs/1905.05172)", with my personal changes to investigate the possibility of using the texture inference network to infer RGB values for a 3D human model.

[Original Project Page (PIFu)](https://shunsukesaito.github.io/PIFu/)<br/>
[Tex2shape Github Repository](https://github.com/thmoa/tex2shape)<br/>
[DensePose Github Respository](https://github.com/facebookresearch/detectron2/tree/master/projects/DensePose)<br/>
![Teaser Image](https://shunsukesaito.github.io/PIFu/resources/images/teaser.png)

The main idea behind this project is to use the texture inference model and apply it to the output of the Tex2shape output. The Tex2shape model produces a more accurate and a higher resolution 3D human model, but without any texture. Because the texture inference network used in PIFu does not rely on a proprietary 3D surface, applying the PIFu texture inference network directly onto the Tex2shape 3D surface should not be an issue (please refer to the <strong>report.pdf</strong> for a detailed summary regarding my exploration).

## Environment & Run
You first will need to create an environment that meets all the requirements for running the original PIFu project. Please refer to the original PIFu repository for details regarding environment setup.

After doing so, you will need to preprocess your input images (generate a mask). You can do this using the following python command:
```python3
# for generating the mask of one example image
python apps/gen_mask.py
```
The file gen_mask.py reads one image. You will need to change your input image to <strong>demo.png</strong> or change the code file. After you have your input image and its corresponding mask, you can follow the original PIFu README.md file to follow through with the rest of the execution.

## Related Research
**[Monocular Real-Time Volumetric Performance Capture (ECCV 2020)](https://project-splinter.github.io/)**
*Ruilong Li\*, Yuliang Xiu\*, Shunsuke Saito, Zeng Huang, Kyle Olszewski, Hao Li*

The first real-time PIFu by accelerating reconstruction and rendering!!

**[PIFuHD: Multi-Level Pixel-Aligned Implicit Function for High-Resolution 3D Human Digitization (CVPR 2020)](https://shunsukesaito.github.io/PIFuHD/)**
*Shunsuke Saito, Tomas Simon, Jason Saragih, Hanbyul Joo*

We further improve the quality of reconstruction by leveraging multi-level approach!

**[ARCH: Animatable Reconstruction of Clothed Humans (CVPR 2020)](https://arxiv.org/pdf/2004.04572.pdf)**
*Zeng Huang, Yuanlu Xu, Christoph Lassner, Hao Li, Tony Tung*

Learning PIFu in canonical space for animatable avatar generation!

**[Robust 3D Self-portraits in Seconds (CVPR 2020)](http://www.liuyebin.com/portrait/portrait.html)**
*Zhe Li, Tao Yu, Chuanyu Pan, Zerong Zheng, Yebin Liu*

They extend PIFu to RGBD + introduce "PIFusion" utilizing PIFu reconstruction for non-rigid fusion.

**[Learning to Infer Implicit Surfaces without 3d Supervision (NeurIPS 2019)](http://papers.nips.cc/paper/9039-learning-to-infer-implicit-surfaces-without-3d-supervision.pdf)**
*Shichen Liu, Shunsuke Saito, Weikai Chen, Hao Li*

We answer to the question of "how can we learn implicit function if we don't have 3D ground truth?"

**[SiCloPe: Silhouette-Based Clothed People (CVPR 2019, best paper finalist)](https://arxiv.org/pdf/1901.00049.pdf)**
*Ryota Natsume\*, Shunsuke Saito\*, Zeng Huang, Weikai Chen, Chongyang Ma, Hao Li, Shigeo Morishima*

Our first attempt to reconstruct 3D clothed human body with texture from a single image!

**[Deep Volumetric Video from Very Sparse Multi-view Performance Capture (ECCV 2018)](http://openaccess.thecvf.com/content_ECCV_2018/papers/Zeng_Huang_Deep_Volumetric_Video_ECCV_2018_paper.pdf)**
*Zeng Huang, Tianye Li, Weikai Chen, Yajie Zhao, Jun Xing, Chloe LeGendre, Linjie Luo, Chongyang Ma, Hao Li*

Implict surface learning for sparse view human performance capture!

------

