import styles from "././Hero.module.css";

const Hero = () => {
  return (
    <>
      <section className={styles.content}>
        <div class={styles.cloud}></div>
        <div class={styles.sun}></div>
        <div class={styles.cloud}></div>
      </section>
      <section className={styles.hero}>
        <p className={styles.title}>Discover songs that go with your mood</p>
        <p className={styles.subtitle}>We just need a picture of you</p>
      </section>
    </>
  );
};

export default Hero;
