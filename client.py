class SpatialObstaclePointcloudVoxelSlicerClient:
    def slice_pointcloud_voxels(self, frame_id='lidar_front_link', point_count=24500, voxel_size_m=0.05, ground_plane_height_m=0.15):
        return {
            'slice_run_id': 'vx_slc_8812',
            'frame_id': frame_id,
            'raw_points_processed': point_count,
            'occupied_voxels_count': 1420,
            'traversable_ground_voxels': 8900,
            'negative_obstacles_detected': 0,
            'minimum_clearance_distance_m': 1.85,
            'occupancy_grid_2_5d_url': 'https://spatial.voxels.genpark.ai/slices/vx_slc_8812.grid'
        }
