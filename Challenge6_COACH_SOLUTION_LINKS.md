# Challenge 5 Coach Guide

## Why we're doing this

## Evaluating Success

## Quick Reference

**CNTK**

* CNTK Object Detection from the great Ari! [info](https://github.com/CatalystCode/CVWorkshop/blob/master/%234%20Policy%20Detection%20with%20Faster%20RCNN.ipynb)

**TensorFlow**

Attention to detail and a couple of hints to avoid some 'gotcha' moments should get you through to running an object detection solution in a short amount of time.

Windows is not a good option for OS when using the Object Detection API. Linux or Unix both work well.

Make sure the API is installed correctly. Not necessarily difficult, but miss a step and you may be spending your day fighting a bad install. Reference the [installation instructions](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md) if you're getting errors, then look into other potential causes.

Start by cloning the tensorflow/models GitHub repository. Most instructions are written to be executed from `tensorflow/models/research/` so you are best off working from that directory. With each new command line session, you will need to run ```export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim```.

* See this [page](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/using_your_own_dataset.md) about using a custom dataset with the object detection API. These are general instructions but are enough to accomplish the task.
* It will be necessary to convert your images and the bounding box information from the tagging tool into TFRecord format for use by the API. There is an out of the box script to show you how to work with [Pascal](https://github.com/tensorflow/models/blob/master/research/object_detection/dataset_tools/create_pascal_tf_record.py) data. There are more examples in this [directory](https://github.com/tensorflow/models/tree/master/research/object_detection/dataset_tools) if needed.
- If you would like another example of how to use a custom dataset with the object detection API, there is a [blog post](https://towardsdatascience.com/how-to-train-your-own-object-detector-with-tensorflows-object-detector-api-bec72ecfe1d9) along with [example code](https://github.com/datitran/raccoon_dataset) that can be helpful to reference.
* When creating TFRecords, make sure to split the data into train and test sets and create `.record` files for each set.
* Create a configuration file that will be used to control the model in training and evaluation. There are also options for data augmentation if desired. Learning rate is specified here.
* There is a template .config for [FasterRCNN](https://github.com/tensorflow/models/blob/master/research/object_detection/faster_rcnn_inception_resnet_v2_atrous_oid.config) that can serve as a starting point and be configured as needed.
* There are several options for FasterRCNN in the model [zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md). If participants are interested, they could swap models and compare accuracies.
* Create a new `.pbtext` file in the correct format as seen [here](https://github.com/tensorflow/models/blob/master/research/object_detection/data/pascal_label_map.pbtxt). Make sure to note that the first id is 1 instead of 0 and it is important to follow this pattern.
* [Medium](https://medium.com/@WuStangDan/step-by-step-tensorflow-object-detection-api-tutorial-part-1-selecting-a-model-a02b6aabe39e)
* Creating a Toy Detector with TF OD API [Ref](https://towardsdatascience.com/building-a-toy-detector-with-tensorflow-object-detection-api-63c0fdf2ac95)
* [stack overflow](https://stackoverflow.com/questions/44973184/train-tensorflow-object-detection-on-own-dataset?noredirect=1&lq=1) question about bringing own data

## Appendix
