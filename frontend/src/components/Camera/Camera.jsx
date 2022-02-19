import styles from "./Camera.module.css";
import { useState } from "react";
import CameraComponent from "react-html5-camera-photo";
import "react-html5-camera-photo/build/css/index.css";

const Camera = () => {
  const [isCameraActive, setIsCameraActive] = useState(false);

  const handlePhoto = (dataUri) => console.log(dataUri);
  const handleClick = () => setIsCameraActive(true);

  return (
    <section className={styles.container}>
      {!isCameraActive ? (
        <button onClick={() => handleClick()} className={styles.button}>
          Take photo
        </button>
      ) : (
        <section className={styles.camera}>
          <CameraComponent
            onTakePhoto={(dataUri) => {
              handlePhoto(dataUri);
            }}
          />
        </section>
      )}
    </section>
  );
};

export default Camera;
