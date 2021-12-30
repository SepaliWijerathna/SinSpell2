import React from 'react';
import '../App.css';

class textArea extends React.Component{
    render(){
        return(
            <form>
                <label style={{ color:'blue'}}>Enter text:
                    <br></br>
                    <textarea className = 'textArea'></textarea>
                </label>
            </form>
        )
    }
    
}

export default textArea;