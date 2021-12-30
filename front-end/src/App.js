import logo from './logo.svg';
import './App.css';
import MainTopic from './components/mainTopic.js'
import TextSection from './components/textSection.js'
import SubTopic from './components/subTopic';
import "./styles/shards-dashboards.1.1.0.min.css";
import SuggestionSection from './components/suggestionSection.js'
import { home } from './home.js'
//import {BrowserRouter, Route, Switch} from 'react-router-dom'
import {
  Container,
  CardBody,
  Button,
  Card
} from "shards-react";
import { suggestion1 } from './data/suggestion.js'
import { useDebugValue, useState } from 'react';
import React from 'react';
import axios from 'axios';


function App() {
  const [value, setValue] = useState("")
  const [suggestion, setSuggestion] = useState(suggestion1)

  function spellCheck() {
    console.log(value)
    axios.get('http://127.0.0.1:8000/', { params: { "word": value } })
      .then(function (response) {
        setSuggestion([response.data])
        console.log(response.data)
      });
  }



  return (
    <div>
      <MainTopic maintopic="SinSpell v 2.0" />
      <div className='row'>
        <div className='column1'>
          <Card small className="mb-4 col-7" align-item-center backgroundColor="ffffff00">
            <CardBody className="border-bottom" >
              <form>
                <label>
                  <h3>Text: </h3>
                  <br></br>
                  <input type="text" value={value} onChange={(e) => {
                    setValue(e.target.value);
                  }}></input>
                  <br></br>
                </label>
              </form>
              <br></br>
              <button onClick={() => {
                spellCheck();
              }}>Check</button>
            </CardBody>
          </Card>
        </div>


        <div className='column2'>
          <Card small className="mb-4 col-7" align-item-center backgroundColor="ffffff00">
            <CardBody className="border-bottom" >
              <h3>Suggestions :</h3>
              <br></br>
              {suggestion.map((data, key) => {
                return (
                  <div key={key}>
                    {"Word : " + data.word}
                    <br></br>
                    <p>Suggestions : </p>
                    <table className='table'>
                      <thead>
                        <tr className='tr'>
                          <th className='th'>Suggested Word</th>
                          <th className='th'>Error Type</th>
                          <th className='th'>Suggested Word Frequency</th>
                          <th className='th'>Error Type Frequency</th>
                          <th className='th'>Percentage</th>
                        </tr>
                      </thead>
                      <tbody>
                        {data.suggestions && data.suggestions.map((s1) => (<>
                          <tr className='tr'>
                            <td className='td'>{s1[0]}</td>
                            <td className='td'>{s1[1]}</td>
                            <td className='td'>{s1[2]}</td>
                            <td className='td'>{s1[3]}</td>
                            <td className='td'>{s1[4]}</td>
                          </tr>
                        </>))

                        }
                      </tbody>
                    </table>



                  </div>
                );
              })}
            </CardBody>
          </Card>
        </div>
      </div>
    </div>

  );
}



export default App;
