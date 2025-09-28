from manim import *

def draw_polygon(
    scene,
    threeDAxes,
    vertices,
    edges=None,
    faces=None,
    vertices_color=RED,
    edge_color=BLUE,
    face_color=YELLOW,
    face_opacity=0.5
):
    """
    - vertices: danh sách toạ độ 3D [[x,y,z], ...]
    - edges: [(i,j), (i,j,"dl"), ...]   # cạnh thường hoặc nét đứt
    - faces: [[i1,i2,i3,...], ...]      # danh sách mặt, mỗi mặt là list các đỉnh
    """

    # Vẽ cạnh
    if edges:
        for e in edges:
            if len(e) == 2:
                start, end = e
                style = "l"
            else:
                start, end, style = e

            start_line = threeDAxes.c2p(*vertices[start])
            end_line = threeDAxes.c2p(*vertices[end])

            if style == "l":
                line = Line(start_line, end_line, color=edge_color)
            elif style == "dl":
                line = DashedLine(start_line, end_line, color=edge_color, dash_length=0.2)

            scene.play(Create(line), run_time=0.1)

    # Vẽ đỉnh
    for v in vertices:
        sphere = Sphere(radius=0.1, color=vertices_color).move_to(threeDAxes.c2p(*v))
        scene.play(Create(sphere), run_time=0.1)

    # Vẽ mặt
    if faces:
        for f in faces:
            pts = [threeDAxes.c2p(*vertices[i]) for i in f]
            poly = Polygon(*pts, color=face_color, fill_opacity=face_opacity)
            scene.play(Create(poly), run_time=0.3)

def animate_edges(scene, threeDAxes, vertices, edges, edge_color=BLUE):
    """
    Animate nhiều cạnh đồng thời.
    edges = [
        (start, end, target_style [, target_color, target_dash, target_opacity]),
        ...
    ]
    Nếu target_color, target_dash, target_opacity không truyền → dùng mặc định.
    """

    animations = []

    for e in edges:
        if len(e) < 3:
            raise ValueError("edges tuple phải có ít nhất (start, end, target_style)")

        start, end, target_style = e[:3]
        target_color = e[3] if len(e) >= 4 else edge_color
        target_dash = e[4] if len(e) >= 5 else 0.2
        target_opacity = e[5] if len(e) >= 6 else 1.0

        start_line = threeDAxes.c2p(*vertices[start])
        end_line = threeDAxes.c2p(*vertices[end])

        # Lấy cạnh hiện tại từ scene nếu đã tồn tại, nếu không tạo mới
        if hasattr(scene, "edge_lines") and (start, end) in scene.edge_lines:
            line_now = scene.edge_lines[(start, end)]
        else:
            if target_style == "l":
                line_now = Line(start_line, end_line, color=target_color, stroke_opacity=target_opacity)
            else:
                line_now = DashedLine(start_line, end_line, color=target_color, dash_length=target_dash, stroke_opacity=target_opacity)
            scene.add(line_now)

        # Tạo cạnh mục tiêu
        if target_style == "l":
            line_target = Line(start_line, end_line, color=target_color, stroke_opacity=target_opacity)
        else:
            line_target = DashedLine(start_line, end_line, color=target_color, dash_length=target_dash, stroke_opacity=target_opacity)

        animations.append(Transform(line_now, line_target))

        # Lưu cạnh hiện tại trong scene để dùng lần sau
        if not hasattr(scene, "edge_lines"):
            scene.edge_lines = {}
        scene.edge_lines[(start, end)] = line_target

    scene.play(*animations, run_time=1)