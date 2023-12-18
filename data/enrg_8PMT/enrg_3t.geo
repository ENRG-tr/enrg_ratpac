// TheiaDetectorFactory recomputes the following geometry components to match
// the values specified in the Theia_PARAMS table

{
name: "GEO",
index: "world",
valid_begin: [0, 0],
valid_end: [0, 0],
mother: "", // world volume has no mother
type: "box",
size: [6000.0, 6000.0, 6000.0], // mm, half-length
material: "rock",
invisible: 1,
}

{
name: "GEO",
index: "hall",
valid_begin: [0, 0],
valid_end: [0, 0],
mother: "world", // world volume has no mother
type: "box",
size: [3000.0, 3000.0, 3000.0], // mm, half-length
material: "air",
invisible: 1,
}

{
name: "GEO",
index: "tank",
valid_begin: [0, 0],
valid_end: [0, 0],
mother: "hall",
type: "tube",
r_max: 760.0,
size_z: 760.0,
position: [0.0, 0.0, 0.0],
material: "steel",
color: [1.0, 0.0, 0.0, 0.1],
drawstyle: "solid"
}

{
name: "GEO",
index: "liner",
valid_begin: [0, 0],
valid_end: [0, 0],
mother: "tank",
type: "tube",
r_max: 755.0,
size_z: 755.0,
position: [0.0, 0.0, 0.0],
material: "pvc_black",
color: [1.0, 0.5, 0.5, 0.1],
drawstyle: "solid"
}

{
name: "GEO",
index: "detector",
valid_begin: [0, 0],
valid_end: [0, 0],
mother: "liner",
type: "tube",
r_max: 750.0,
size_z: 750.0,
position: [0.0, 0.0, 0.0],
material: "water_gd_0p1", //gd-loaded water, 0.1% in mass
// material: "wbls_10pct",
//material: "wbls_5pct_gdS_0p2",
color: [0.6, 0.8, 1.0, 0.9],
drawstyle: "solid"
}

{ 
name: "GEO", 
index: "inner_pmts", 
enable: 1,
valid_begin: [0, 0], 
valid_end: [0, 0], 
mother: "detector", 
type: "pmtarray", 
pmt_model: "r5912_hqe",
pmt_detector_type: "idpmt",
sensitive_detector: "/mydet/pmt/inner", 
efficiency_correction: 1.000,
light_cone: 0,  
pos_table: "PMTINFO", //generated on the fly
//  //  start_idx: 0, //index of first inner pmt
//  // end_idx: 0, //index of last inner pmt
orientation: "manual",
//  // orient_point: [0.0, 0.0, 0.0],
} 

// { 
// name: "GEO", 
// index: "veto_pmts",
// enable: 1,
// valid_begin: [0, 0], 
// valid_end: [0, 0], 
// mother: "detector", 
// type: "pmtarray", 
// pmt_model: "r11780_hqe",
// pmt_detector_type: "idpmt",
// sensitive_detector: "/mydet/pmt/veto", 
// efficiency_correction: 1.000,  
// pos_table: "PMTINFO", //generated on the fly
// start_idx: 0, //index of first veto pmt
// end_idx: 0, //index of last veto pmt
// orientation: "manual",
// } 


