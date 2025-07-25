/**
 * 📘 INTRODUÇÃO AO REACT
 *
 * React é uma biblioteca JavaScript para construção de interfaces de usuário (UIs).
 * Criado pelo Facebook, é baseado em **componentes reutilizáveis** e em um fluxo de dados unidirecional.
 *
 * ➕ Ideal para SPAs (Single Page Applications)
 * ➕ Utiliza JSX, que mistura HTML + JS de forma declarativa
 * ➕ Trabalha com virtual DOM para melhor desempenho
 *
 * Instalação com Vite (recomendado):
 * 1. npm create vite@latest meu-projeto -- --template react
 * 2. cd meu-projeto
 * 3. npm install
 * 4. npm run dev
 */

// 📌 EXEMPLO DE COMPONENTE FUNCIONAL SIMPLES

function Saudacao() {
  return (
    <div>
      <h1>Olá, desenvolvedor!</h1>
      <p>Seja bem-vindo ao React 👋</p>
    </div>
  );
}

// Esse componente pode ser usado dentro de outro como <Saudacao />

// 📌 COMPONENTE COM PROPRIEDADES (props)

function BemVindo(props) {
  return <h2>Bem-vindo(a), {props.nome}!</h2>;
}

// <BemVindo nome="Victor" /> → renderiza: "Bem-vindo(a), Victor!"

// 📌 COMPONENTE COM ESTADO (state)
// Hooks como useState permitem controlar dados dinâmicos

import { useState } from 'react';

function Contador() {
  const [contador, setContador] = useState(0); // estado inicial = 0

  return (
    <div>
      <p>Valor atual: {contador}</p>
      <button onClick={() => setContador(contador + 1)}>Incrementar</button>
    </div>
  );
}

// Toda vez que o botão é clicado, o estado muda e o componente re-renderiza

// 📌 EVENTOS EM REACT
// Usa camelCase, como onClick, onChange, etc.

function Formulario() {
  const [nome, setNome] = useState('');

  function enviarFormulario(e) {
    e.preventDefault();
    alert(`Formulário enviado por ${nome}`);
  }

  return (
    <form onSubmit={enviarFormulario}>
      <input
        type="text"
        placeholder="Digite seu nome"
        value={nome}
        onChange={(e) => setNome(e.target.value)}
      />
      <button type="submit">Enviar</button>
    </form>
  );
}

// 📌 LISTAS E CHAVES ÚNICAS

const linguagens = ['JavaScript', 'Python', 'Dart'];

function ListaLinguagens() {
  return (
    <ul>
      {linguagens.map((lang, index) => (
        <li key={index}>{lang}</li>
      ))}
    </ul>
  );
}

// Sempre usar uma key única ao renderizar listas dinâmicas

// 📌 ESTRUTURA DE UM PROJETO COM VITE

/**
 * src/
 * ├── App.jsx           // Componente principal
 * ├── main.jsx          // Ponto de entrada (renderiza App)
 * ├── components/       // Componentes reutilizáveis
 * └── assets/           // Imagens, CSS, ícones
 */

// main.jsx

import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// App.jsx

export default function App() {
  return (
    <div>
      <Saudacao />
      <BemVindo nome="Victor" />
      <Contador />
      <Formulario />
      <ListaLinguagens />
    </div>
  );
}

/**
 * 🛠 PRINCIPAIS CONCEITOS DO REACT:
 * - Componentização (reutilização)
 * - Estado e ciclo de vida (useState, useEffect)
 * - Props para comunicação entre componentes
 * - JSX para sintaxe declarativa
 * - Unidirecional: dados fluem dos pais para os filhos
 *
 * 🎯 DICA FINAL:
 * Estude o uso de hooks modernos como:
 * - useState
 * - useEffect
 * - useContext
 * - useRef
 *
 * A documentação oficial é excelente e didática:
 * https://react.dev/learn
 */

