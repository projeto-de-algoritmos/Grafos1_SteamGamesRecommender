// import logo from './logo.svg';
import './App.css';
import React, {useState, useEffect} from 'react';
import ReactDOM from 'react-dom';
import Graph from 'react-vis-network-graph';
import AsyncSelect from 'react-select/async';

import axios from 'axios';

import options from './VisOptions'

function App() {

  const [selected, setSelected] = useState();
  // const [appid, setAppId] = useState();
  const [name, setName] = useState("");
  const [list, setList] = useState([]);
  const [network, setNetwork] = useState();

  const [graph, setGraph] = useState();

  const loadOptions = (inputvalue, callback) => {
    axios.get(`http://localhost:5000/search/${inputvalue}`).then(
      (response) => {
        callback(JSON.parse(response.data))
      }
    ).catch((err) => {
      console.log(err)
    })
  }

  const handleSelection = (e) => {
    setSelected(e.value)
  }

  const inputChange = (value) => {
    setName(value);
  }

  const submit = () => {
    console.log(`selected = ${selected}`);
    axios.get(`http://localhost:5000/graph/${selected}`).then(
      (response) => {
        network.setData(response.data)
      }
    ).catch((err) => {
      console.log(err)
    })
  }

  return (
    <div id="all">
      <div id="Header"><spam>SteamGamesRecommender</spam></div>
      <div id="Search">
        <AsyncSelect cacheOptions loadOptions={loadOptions} onInputChange={inputChange} onChange={handleSelection}/>
        <button onClick={submit}>Search</button>
      </div>
      <Graph options={options} style={options.style} getNetwork={network => setNetwork(network)}/>
    </div>
  );
}

export default App;
