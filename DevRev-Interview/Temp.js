import React, { useState } from "react";

const Temp = (props) => {
  // Red Green Blue
  const [color1, setColor1] = useState("red");
  const [color2, setColor2] = useState("green");
  const [color3, setColor3] = useState("blue");

  const dot = {
    height: "50px",
    width: "50px",
    borderRadius: "50%",
    display: "inline-block",
    margin: "10px",
  };

  const changeColour = () => {
    if (color3 == "red") {
      setColor3("blue");
    } else {
      setColor3("red");
    }
  };
  return (
    <div>
      <span
        style={{ ...dot, backgroundColor: color1 }}
        onClick={() => {
          changeColour();
        }}
      ></span>
      <span className="dot" style={{ ...dot, backgroundColor: color2 }}></span>
      <span className="dot" style={{ ...dot, backgroundColor: color3 }}></span>
    </div>
  );
};

export default Temp;
