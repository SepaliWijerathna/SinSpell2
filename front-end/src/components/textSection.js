import React from 'react';
import {
    Container,
    CardBody,
    Button,
    Card
  } from "shards-react";
  import TextArea from './textArea';
  import Section from './section';
  import '../App.css';
  import SubmitButton from './button';

class textSection extends React.Component{
    constructor(){
        super()
        this.state = {

        }
    }

    check(){
        this.setState({
            
        })
    }


    render(){
        return (  
            <div className = 'column'>
                <Card small className="mb-4 col-7"  align-item-center backgroundColor = "ffffff00">
                    <CardBody className="border-bottom" >
                    <TextArea></TextArea>
                    <button onClick={() => this.check()}>Check</button>
                    </CardBody>
                </Card>
            </div>       
            
        )
    }    
} 


export default textSection;