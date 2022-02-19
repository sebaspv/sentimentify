import styles from "./Footer.module.css";

const Footer = () => {
  return (
    <footer className={styles.footer}>
      <p
        className={styles.title}
      >{`©️ ${new Date().getFullYear()} - Pumas Team`}</p>
    </footer>
  );
};

export default Footer;
