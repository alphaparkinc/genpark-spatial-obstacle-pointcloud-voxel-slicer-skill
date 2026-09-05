from client import SpatialObstaclePointcloudVoxelSlicerClient

def main():
    client = SpatialObstaclePointcloudVoxelSlicerClient()
    res = client.slice_pointcloud_voxels()
    print('Voxel Slicer: ' + res['slice_run_id'] + ' (' + str(res['raw_points_processed']) + ' pts)')
    print('Occupied: ' + str(res['occupied_voxels_count']) + ' | Min Clearance: ' + str(res['minimum_clearance_distance_m']) + 'm')
    print('Grid URL: ' + res['occupancy_grid_2_5d_url'])

if __name__ == '__main__':
    main()
