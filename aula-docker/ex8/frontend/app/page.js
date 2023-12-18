"use client";
import React, { useState } from "react";
import styles from "./page.module.css";

export default function Home() {
  const [resultado, setResultado] = useState("teste");

  async function fazerRequisicao() {
    try {
      const response = await fetch("http://backend:8000/");
      const data = await response.json();
      setResultado(data["message"]);
    } catch (err) {
      alert("Requisição não foi realizada");
    }
  }

  return (
    <main className={styles.main}>
      <button style={{ padding: 10, margin: 10 }} onClick={fazerRequisicao}>
        Fazer requisição
      </button>
      <div>Resultado: {resultado}</div>
    </main>
  );
}
