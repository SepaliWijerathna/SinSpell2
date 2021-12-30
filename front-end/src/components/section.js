import React from 'react';
import {
    Container,
    CardBody,
    Button,
    Card
  } from "shards-react";
  import TextArea from './textArea';

class section extends React.Component{
    render(){
        return (
            <div className = 'colomn'>
                <Card small className="mb-4 col-7"  align-item-center backgroundColor = "ffffff00">
                    <CardBody className="border-bottom" >
                    </CardBody>
                </Card>
            </div>
           
            
        )
    }    
} 


export default section;