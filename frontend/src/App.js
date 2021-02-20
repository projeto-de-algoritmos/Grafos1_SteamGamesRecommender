// import logo from './logo.svg';
import './App.css';
import React, {useState, useEffect} from 'react';
import ReactDOM from 'react-dom';
import Graph from 'react-vis-network-graph';

function App() {

  const graph = {
    nodes: [
      {id: 25484, label: "teste"},
      {id: 123, label: "teste2"},
      {id: 85184, label: "teste3"}
    ],
    edges: [
      {from: 25484, to: 123},
      {from: 123, to: 85184},
      {from: 85184, to: 25484}
    ]
  }
  
  const options = {
    edges: {
      arrows: {
        to: {
          enabled: false
        }
      }
    }
  }

  const style = {
    height: '90%',
    width: '75%'
  }

  return (
    <div id="all">
      <div id="Header">SteamGamesRecommender</div>
      <div id="Search"></div>
      <Graph graph={graph} options={options} style={style}/>
    </div>
  );
}

export default App;
