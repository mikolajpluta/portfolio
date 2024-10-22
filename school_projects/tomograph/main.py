import streamlit as st
from PIL import Image
from tomograph import Tomograph
import pydicom
import datetime
import numpy
from pydicom.dataset import FileDataset, FileMetaDataset
import tempfile
import pydicom._storage_sopclass_uids

tomograph2 = None


def main():
    global tomograph2
    st.title("Tomograf")
    st.write("Proszę wypełnić poniższe pola.")

    ID = st.text_input("ID pacjenta:", value=st.session_state.get("ID"))
    imie = st.text_input("Imie i nazwisko:", value=st.session_state.get("imie"))
    wiek = st.text_input("Wiek:", value=st.session_state.get("wiek"))
    ID_badania = st.text_input("ID badania:", value=st.session_state.get("ID_badania"))
    data_badania = st.text_input("Data Badania:", value=st.session_state.get("date"))
    numer_serii = st.text_input("Numer Serii:", value=st.session_state.get("numer_serii"))
    komentarz = st.text_input("Komentarz:", value=st.session_state.get("komentarz"))
    czas_badania = st.text_input("Czas badania:", value=st.session_state.get("czas") )

    # Wprowadzenie danych użytkownika
    if "imie" not in st.session_state:
        st.session_state['imie'] = imie
        st.session_state['date'] = data_badania
        st.session_state['wiek'] = wiek
        st.session_state['komentarz'] = komentarz
        st.session_state['ID'] = ID
        st.session_state['ID_badania'] = ID_badania
        st.session_state['numer_serii'] = numer_serii
        st.session_state["czas"] = czas_badania


    # Wprowadzenie parametrów tomografu
    alpha = st.number_input("Kąt alpha:", min_value=1, max_value=360, step=1)
    angular_span = st.number_input("Rozpiętość kątowa:", min_value=1, max_value=360, step=1)
    sensor_quantity = st.number_input("Ilość sensorów:", min_value=1, step=1)

    # Wczytanie obrazu
    uploaded_file = st.file_uploader("Wybierz obraz do analizy:", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.session_state["uploaded"] = uploaded_file
        st.session_state["dicom_file"] = False

    if st.button("Wczytaj dane z obrazu") and uploaded_file is not None:
        st.session_state["dicom_file"] = False
        st.session_state["uploaded"] = uploaded_file

    if st.button("Generuj Obraz"):
        uploaded_file = st.session_state.get("uploaded")

        if not st.session_state["dicom_file"]:
            image = Image.open(uploaded_file)
        else:
            image = uploaded_file

        tomograph = Tomograph(alpha, angular_span, sensor_quantity, image)

        tomograph.calculate_points()

        for i in range(360 // alpha):
            tomograph.sinogram_step()
            tomograph.step += 1
            tomograph.calculate_points()

        sinogram = tomograph.get_sinogram_image()
        if sinogram is not None:
            st.image([image, sinogram], caption=["Wybrany obraz", "Sinogram"], width=350)

        tomograph.step = 0
        tomograph.calculate_points()

        for i in range(360 // alpha):
            for n in range(sensor_quantity):
                tomograph.sum_brightness(tomograph.emiters[n], tomograph.detectors[-1 - n], tomograph.sinogram[i][n])
            tomograph.step += 1
            tomograph.calculate_points()

        final = tomograph.draw_final_image()
        st.session_state["max_val"] = tomograph.max_val
        print("max val 1: ", tomograph.max_val)
        if final is not None:
            st.image([final], caption=["Final Image"], width=350)
            st.session_state["final_to_save"] = final

    if st.button("Uruchamiaj krokowo"):
        uploaded_file = st.session_state.get("uploaded")
        if not st.session_state["dicom_file"]:
            image = Image.open(uploaded_file)
        else:
            image = uploaded_file
        st.session_state["uploaded"] = image

        tomograph2 = Tomograph(alpha, angular_span, sensor_quantity, image)
        tomograph2.calculate_points()
        st.session_state["tomograph2"] = tomograph2
        tomograph2.step = 0
        tomograph2.make_sinogram_step_image()
        sinogram = tomograph2.sinogram_step_image
        tomograph2.draw_step()
        final = tomograph2.img_state
        st.image([image, sinogram], caption=["Wybrany obraz", "Sinogram"], width=350)
        st.image([final], caption="Obraz Wynikowy", width=350)
        st.session_state["max_steps"] = 360 // alpha
        st.session_state["current_step"] = 0

    if st.button("Krok"):
        st.session_state["current_step"] += 1
        if st.session_state["current_step"] < st.session_state["max_steps"]:
            tomograph2 = st.session_state.get("tomograph2")

            if tomograph2 is not None:
                image = st.session_state.get("uploaded")
                tomograph2.step += 1
                tomograph2.calculate_points()
                tomograph2.sinogram_step()

                for n in range(sensor_quantity):
                    tomograph2.sum_brightness(tomograph2.emiters[n], tomograph2.detectors[-1 - n], tomograph2.sinogram[tomograph2.step][n])

                tomograph2.make_sinogram_step_image()
                sinogram = tomograph2.sinogram_step_image

                final = tomograph2.draw_final_image()
                st.image([image, sinogram], caption=["Wybrany obraz", "Sinogram"], width=350)
                st.image([final], caption="Obraz Wynikowy", width=350)
                st.session_state["final"] = final
                st.session_state["sinogram"] = sinogram
                st.session_state["final_to_save"] = final
        else:
            final = st.session_state.get("final")
            sinogram = st.session_state.get("sinogram")
            image = st.session_state.get("uploaded")
            st.image([image, sinogram], caption=["Wybrany obraz", "Sinogram"], width=350)
            st.image([final], caption="Obraz Wynikowy", width=350)
            st.session_state["final_to_save"] = final
            st.toast("Wykonano już wszystkie kroki, obraz wynikowy gotowy do zapisania")

    uploaded_dicom = st.file_uploader("Wybierz plik DICOM:", type=["dcm"])

    if uploaded_dicom is not None:
        dicom_data = pydicom.dcmread(uploaded_dicom)
        st.text(dicom_data)
        if "PatientName" in dicom_data:
            st.session_state.imie = dicom_data.PatientName
        if "PatientAge" in dicom_data:
           st.session_state.wiek = dicom_data.PatientAge
        if "StudyDate" in dicom_data:
            st.session_state.date = dicom_data.StudyDate
        if "StudyDescription" in dicom_data:
            st.session_state.komentarz = dicom_data.StudyDescription
        if "PatientID" in dicom_data:
            st.session_state.ID = dicom_data.PatientID
        if "SeriesNumber" in dicom_data:
            st.session_state.numer_serii = dicom_data.get(0x00200011).value #numer hexadecymalny pola 'numer serii' w pliku dicom
        if "StudyID" in dicom_data:
            st.session_state.ID_badania = dicom_data.get(0x00200010).value #tak jak powyzej
        if "StudyTime" in dicom_data:
            st.session_state.czas = dicom_data.get(0x00080030).value #tak samo
        st.session_state["dicom_file"] = dicom_data

    if st.button("Wczytaj z pliku DICOM") and uploaded_dicom is not None:
        dicom_data = st.session_state.get("dicom_file")

        image = Image.fromarray(dicom_data.pixel_array)
        st.session_state.uploaded = image
        if "PatientName" in dicom_data:
            st.session_state.imie = dicom_data.PatientName
        if "PatientAge" in dicom_data:
           st.session_state.wiek = dicom_data.PatientAge
        if "StudyDate" in dicom_data:
            st.session_state.date = dicom_data.StudyDate
        if "StudyDescription" in dicom_data:
            st.session_state.komentarz = dicom_data.StudyDescription
        if "PatientID" in dicom_data:
            st.session_state.ID = dicom_data.PatientID
        if "SeriesNumber" in dicom_data:
            st.session_state.numer_serii = dicom_data.get(0x00200011).value #numer hexadecymalny pola 'numer serii' w pliku dicom
        if "StudyID" in dicom_data:
            st.session_state.ID_badania = dicom_data.get(0x00200010).value #tak jak powyzej
        if "StudyTime" in dicom_data:
            st.session_state.czas = dicom_data.get(0x00080030).value #tak samo


    if st.button("Zapisz do DICOM"):
        suffix = '.dcm'
        filename_little_endian = tempfile.NamedTemporaryFile(suffix=suffix).name

        file_meta = FileMetaDataset()
        file_meta.preamble = b"DICM"
        file_meta.MediaStorageSOPClassUID = pydicom._storage_sopclass_uids.CTImageStorage
        file_meta.MediaStorageSOPInstanceUID = pydicom.uid.generate_uid()
        file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian  
        file_meta.ImplementationVersionName = '1.0'  

        ds = FileDataset(filename_little_endian, {}, preamble=b"\0" * 128)
        ds.file_meta = file_meta

        ds.PatientName = imie
        ds.PatientAge = wiek
        ds.StudyDate = data_badania
        ds.StudyDescription = komentarz
        ds.PatientID = ID
        ds.SeriesNumber = numer_serii
        ds.StudyID = ID_badania
        ds.StudyTime = czas_badania


        ds.SOPClassUID = pydicom._storage_sopclass_uids.CTImageStorage
        ds.SOPInstanceUID = file_meta.MediaStorageSOPInstanceUID
        ds.Modality = "CT"
        ds.SeriesInstanceUID = pydicom.uid.generate_uid()
        ds.StudyInstanceUID = pydicom.uid.generate_uid()
        ds.FrameOfReferenceUID = pydicom.uid.generate_uid()

        ds.ImageType = r"ORIGINAL\PRIMARY\AXIAL"
        ds.SamplesPerPixel = 1
        ds.PixelRepresentation = 0
        ds.BitsStored = 8
        ds.BitsAllocated = 8
        ds.HighBit = 7
        ds.ImagesInAcquisition = 1
        ds.InstanceNumber = 1
        ds.PhotometricInterpretation = "MONOCHROME2"
        image = st.session_state.get("final_to_save")
        image = image.convert('L')

        pixel_data = numpy.array(image, dtype=numpy.uint8)
        
        ds.Rows = pixel_data.shape[0]
        ds.Columns = pixel_data.shape[1]
        ds.PixelData = pixel_data.tobytes()

        ds.is_little_endian = True
        ds.is_implicit_VR = False

        dt = datetime.datetime.now()
        ds.ContentDate = dt.strftime('%Y%m%d')
        timeStr = dt.strftime('%H%M%S.%f')  # long format with micro seconds
        ds.ContentTime = timeStr
        pydicom.dataset.validate_file_meta(ds.file_meta, enforce_standard=True)
        # Zapisz obiekt Dataset do pliku DICOM
        ds.save_as("generated_dicom.dcm", write_like_original=False)
        st.toast("Plik został zapisany pomyślnie pod nazwą: generated_dicom.dcm")


if __name__ == "__main__":
    main()
