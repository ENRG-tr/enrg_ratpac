// taken from: https://github.com/vfischer/ANNIEratpac/blob/annie/data/ANNIE/ANNIE_AmBesource.geo

//this i going to creat a wire has a radius of 3.0 and lenght of 315.75
// we are tryng to creta a wire for half of the detector.
// half of the dedector is 750.0 and we should use half of that lenght which is 375.0
// we subtract the z pozition of the "AmBe_wires_vertical" 375-36.5 = 338.5
// add the  radius of wire  which is 3
// 338.5+3 = 341.5

{
name: "GEO",
index: "AmBe_wires_horizantal", //represents the black bag with the wires inside
enable: 1,
valid_begin: [0, 0],
valid_end: [0, 0],
mother: "detector",
type: "tube",
r_max: 3.0,
size_z: 341.5,  
position: [0.0, 150.0, 375.0], // position is housing body position + 19 cm in Z
material: "acrylic_black",
color: [0.3, 0.3, 0.3, 0.3],
drawstyle: "solid",
}



// we need another wire connect the wire amd AmBe housing
// this wire shoul be radius of 3 and length of 150 because we choose this y-position for AmBe-wires-horizantal
// to draw 150.0 we need half of that whic is 75.0
// we need to substract the half of the AmBe_housing_body size_z = 68.5  an half of that 34.25
// to draw this we need half of that 17.125  >>> 75- 17.125 = 57.875

// to start correct position  we need to add 17.125 to the 75 and use as y-position 75+17.125= 92.125
// to rotate the wire used x ration as 90 deg

{
name: "GEO",
index: "AmBe_wires_vertical", //represents the black bag with the wires inside
enable: 1,
valid_begin: [0, 0],
valid_end: [0, 0],
mother: "detector",
type: "tube",
r_max: 3.0,
size_z: 57.875,
position: [0.0, 92.125, 36.5], // position is housing body position + 19 cm in Z
rotation: [90.0, 0.0, 0.0]
material: "acrylic_black",
color: [0.3, 0.3, 0.3, 0.3],
drawstyle: "solid",
}

{
name: "GEO",
index: "AmBe_housing_body",
enable: 1,
valid_begin: [0, 0],
valid_end: [0, 0],
mother: "detector",
type: "tube",
r_max: 35.0,
size_z: 68.5,
position: [0.0, 0.0, 63.5], //Center (AmBe source not housing) is [0.0, 0.0, 64.55], Axis are [+MITPC/-stairs;+FMV/-MRD;+top/-bottom]
material: "acrylic_uvt", 
surface: "ptfe",
color: [0.0, 1.0, 1.0, 0.1],
drawstyle: "solid",
}

{
name: "GEO",
index: "AmBe_housing_air",
enable: 1,
valid_begin: [0, 0],
valid_end: [0, 0],
mother: "AmBe_housing_body",
type: "tube",
r_max: 25.0,
size_z: 56.0,
position: [0.0, 0.0, 0.0],
material: "air", 
color: [0.0, 1.0, 1.0, 0.1],
drawstyle: "solid",
}

{
name: "GEO",
index: "AmBe_housing_cap", //represents the cap of the housing
valid_begin: [0, 0],
valid_end: [0, 0],
mother: "AmBe_housing_air",
type: "revolve",
r_max: [25.0, 25.0, 35.0, 35.0, 20.0],
r_min: [0.0, 0.0, 0.0, 0.0, 0.0],
z: [0.0, 15.0, 15.1, 20.0, 45.0],
position: [0.0, 0.0, 53.5],
material: "acrylic_uvt", 
surface: "ptfe",
color: [0.0, 1.0, 1.0, 0.1],
drawstyle: "solid",
}

{
name: "GEO",
index: "AmBe_BGO",
enable: 1,
valid_begin: [0, 0],
valid_end: [0, 0],
mother: "AmBe_housing_air",
type: "tube",
r_max: 25.0,
size_z: 25.0,
position: [0.0, 0.0, -20.0],
material: "BGO_scint",
color: [0.0, 0.3, 1.0, 0.1],
drawstyle: "solid",
}

{
name: "GEO",
index: "AmBe_placer",
valid_begin: [0, 0],
valid_end: [0, 0],
mother: "AmBe_housing_air",
type: "tube",
r_max: 25.0,
size_z: 5.5,
position: [0.0, 0.0, -50.5],
material: "acrylic_uva_McMaster",
color: [0.0, 1.0, 1.0, 0.5],
drawstyle: "solid",
}

{
name: "GEO",
index: "AmBe_case",
valid_begin: [0, 0],
valid_end: [0, 0],
mother: "AmBe_placer",
type: "tube",
r_max: 2.5,
size_z: 2.5,
position: [0.0, 0.0, -2.5],
material: "stainless_steel",
color: [0.0, 1.0, 1.0, 0.7],
drawstyle: "solid",
}

{
name: "GEO",
index: "AmBe_source",
valid_begin: [0, 0],
valid_end: [0, 0],
mother: "AmBe_case",
type: "tube",
r_max: 0.5,
size_z: 0.5,
position: [0.0, 0.0, 0.0],
material: "beryllium",
color: [0.0, 1.0, 1.0, 0.9],
drawstyle: "solid",
}
