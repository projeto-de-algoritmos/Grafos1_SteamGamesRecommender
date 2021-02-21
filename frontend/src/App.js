// import logo from './logo.svg';
import './App.css';
import React, {useState, useEffect} from 'react';
import ReactDOM from 'react-dom';
import Graph from 'react-vis-network-graph';
import AsyncSelect from 'react-select/async';

import axios from 'axios';

function App() {

  const api = axios.create({
    baseURL: "localhost:5000"
  })
  const [selected, setSelected] = useState();
  // const [appid, setAppId] = useState();
  const [name, setName] = useState("");
  const [list, setList] = useState([]);
  const [network, setNetwork] = useState();

  const [graph, setGraph] = useState({
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
  });

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

  const loadOptions = (inputvalue, callback) => {
    // api.get(`/search/${inputvalue}`).then(
    //   (Response) => {
    //     // tratar Response
    //     callback(Response)
    //   }
    // )
    setTimeout(() => {
      callback([
        {value: "abc", label: "teste"}
      ])
    }, 1000)
  }

  const handleSelection = (e) => {
    setSelected(e.value)
  }

  const inputChange = (value) => {
    setName(value);
  }

  const submit = () => {
    // api.get(`/${selected}`).then(
    //   (Response) => {
    //     setGraph(Response)
    //   }
    // )

    // setGraph({})
    
    network.setData({
      nodes: [
        {id: 1, label: "a"},
        {id: 2, label: "b"},
        {id: 3, label: "c"}
      ],
      edges: [
        {from: 1, to: 2},
        {from: 3, to: 1},
      ]})
  }

  return (
    <div id="all">
      <div id="Header">SteamGamesRecommender</div>
      <div id="Search">
        <AsyncSelect cacheOptions loadOptions={loadOptions} onInputChange={inputChange} onChange={handleSelection}/>
        <button onClick={submit}>Search</button>
      </div>
      <Graph graph={graph} options={options} style={style} getNetwork={network => setNetwork(network)}/>
    </div>
  );
}

export default App;
