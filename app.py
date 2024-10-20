import cv2

def add_text_to_video(video_path, output_path, text):
    # Split text by ';' to get individual lines
    lines = text.split(';')

    # Open the video
    cap = cv2.VideoCapture(video_path)

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate frame range per line of text
    frames_per_line = total_frames // len(lines)

    # VideoWriter to save the output video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    frame_idx = 0
    current_line_idx = 0

    # Iterate through each frame
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # Calculate which text line to display
        if frame_idx // frames_per_line != current_line_idx:
            current_line_idx += 1

        if current_line_idx < len(lines):
            # Add text to the frame with black color and increased font size
            cv2.putText(frame, lines[current_line_idx], (50, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3, cv2.LINE_AA)

        # Write the frame to the output video
        out.write(frame)

        frame_idx += 1

    # Release everything when done
    cap.release()
    out.release()

# Example usage
video_path = 'input_video.mp4'
output_path = 'output_video.avi'
text = "This is the first line;This is the second line;This is the third line"
add_text_to_video(video_path, output_path, text)
