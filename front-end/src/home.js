import React from 'react';
import './App.css';
import MainTopic from './components/mainTopic.js'
import TextSection from './components/textSection.js'
import SubTopic from './components/subTopic';
import "./styles/shards-dashboards.1.1.0.min.css";
import SuggestionSection from './components/suggestionSection.js'

export class home extends React.Component{
    render(){
        return(
            <div>
                <MainTopic maintopic = "SinSpell v 2.0"/>  
                <div className = 'row'>
                    <TextSection />
                    <SuggestionSection />
                </div>
            </div>
        )
    }
}