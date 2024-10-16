import pymeshlab

# สร้าง MeshSet
ms = pymeshlab.MeshSet()

print("Loading point cloud...")
# โหลด point cloud
ms.load_new_mesh('C:\\test\\pointcloud.ply')

print("Computing normals...")
# คำนวณ normals สำหรับ point cloud
ms.compute_normal_for_point_clouds()

print("Generating mesh using ball pivoting algorithm...")
# แปลง point cloud เป็น mesh ด้วย ball pivoting algorithm
ms.generate_surface_reconstruction_ball_pivoting()

print("Saving mesh...")
# บันทึก mesh ที่สร้างขึ้น
ms.save_current_mesh('C:\\test\\output_mesh.obj')

print("Mesh saved successfully!")