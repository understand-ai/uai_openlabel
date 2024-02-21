# Example OpenLABEL JSONs

These examples are taken from the original ASAM OpenLABEL specification document 
([link](https://www.asam.net/index.php?eID=dumpFile&t=f&f=4566&token=9d976f840af04adee33b9f85aa3c22f2de4968dd)).
Descriptions of the example files are also taken mostly from the document. 

> These tests deserialize and re-serialize the example files and make sure they match. 

Not all example files from the original document are yet in here, because they use data types that aren't implemented yet. 
These include files found in section `7.12.3. Point clouds`, `7.12.4. Semantic segmentation`. 

### modified_19_vegetation_curve_19.1_labels.json

From the dataset published by the Deutsche Bahn: https://digitale-schiene-deutschland.de/en/news/2023/OSDaR23-multi-sensor-data-set-for-machine-learning. 
Additional fields that are not in the vanilla ASAM OpenLABEL format have been removed. 

Citation: 
```
Roman Tilly , Philipp Neumaier , Karsten Schwalbe , Pavel Klasek , Rustam Tagiew , Patrick Denzler , Tobias Klockau , Martin Boekhoff , Martin Köppel , (2023). 
Open Sensor Data for Rail 2023 [Data set]. 
TIB. https://doi.org/10.57806/9mv146r0
```

### openlabel100_test_bbox_simple.json

From section `7.12.1 2D bounding boxes`, this JSON contains simple bounding boxes.
Besides the `metadata` tag, this OpenLABEL example only makes use of the `objects` tag - no `frames`! 

### openlabel100_test_bbox_simple_attributes.json

From section `7.12.1 2D bounding boxes`, this JSON contains extended properties of objects and bounding boxes. 
Besides the `metadata` tag, this OpenLABEL example only makes use of the `objects` tag - no `frames`! 

### openlabel100_example_cuboids.json

From section `7.13.1  3D bounding boxes (cuboids)`, this JSON contains the labels for an entire scene, 
including transform entries for all frames representing the odometry values obtained with a differential GPS.

This use case shows an example of 3D bounding boxes (or cuboids) labels. The example shows the creation of 
object labels in a sequence of point clouds obtained from a LiDAR sensor. 
Labels correspond to physical objects, that is, cars and pedestrians.

In this example, the cuboids are expressed using the preferred quaternion-translation vector form, 
which implies that ten values define the cuboid data, as explained in 3D bounding box (cuboid).


