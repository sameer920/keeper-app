import React from "react";

let year = new Date().getFullYear();

function footer(){
    return <footer><p>CopyRight Keeper App ⓒ {year}</p></footer>
}

export default footer;