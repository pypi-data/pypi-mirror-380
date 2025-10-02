from krita import Krita


def __main__(*args):
    width = args[0][0]
    height = args[0][1]
    frame_rate = args[0][2]
    frame_count = args[0][3]
    file_path = args[0][4]
    file_name = args[0][5]

    app = Krita.instance()

    doc = app.createDocument(
        int(width), int(height), file_name, "RGBA", "U16", "", 96.0
    )

    doc.setFramesPerSecond(int(frame_rate))
    doc.setFullClipRangeEndTime(int(frame_count))

    # image_sequence_path = "C:/Users/lucile.leboullec/Documents/libreflow_dev/demoproject_files/demoproject/sq001/sh010/layout/v002/animatique_image_sequence"
    # files = os.listdir(image_sequence_path)
    # for i in range(0, len(files)):
    #     files[i] = f"{image_sequence_path}/{files[i]}"

    # doc.importAnimation(files, 0, 1)

    doc.saveAs(file_path)
