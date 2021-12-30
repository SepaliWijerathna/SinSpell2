import React from 'react';
import {
    Container,
    CardBody,
    Button,
    Card
  } from "shards-react";
  import '../App.css';
  import { suggestion1 } from '../data/suggestion.js'
  

class suggestionSection extends React.Component{
    render(){
        return (
            <div className = 'column'>
                <Card small className="mb-4 col-7"  align-item-center backgroundColor = "ffffff00">
                    <CardBody className="border-bottom" >
                        <h3>suggestions</h3>
                        {suggestion1.map((data, key) => {
                            return (
                              <div key={key}>
                                {"word : " + data.word }
                                <br></br>
                                {"suggestions : " + data.suggestions.join("\n") }
                                

                              </div>
                            );
                          })}
                    </CardBody>
                </Card>
            </div>         
            
        )
    }    
} 


export default suggestionSection;