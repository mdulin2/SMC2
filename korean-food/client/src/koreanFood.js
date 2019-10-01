import React, { Component } from "react";
import "./App.css";
import axios from "axios";

class koreanFood extends Component {
  // Essentially global state variables
  state = {
    koreanFoodName: "",
    koreanFoodSearch: [],
	isAuth: false
  };

  componentDidMount(){
	  this.authCheck();
  }
  
  // Update the value of the korean food variable
  onKeyDownKoreanFood = event => {
    // events are passed in by the event
    this.setState({ koreanFoodName: event.target.value });
  };

  // Action for clicking the search button
  onClickSearch = async () => {
    const searchResponse = await axios.post("/koreanFood", {
      food_name: this.state.koreanFoodName
    });
    this.setState({ koreanFoodSearch: searchResponse.data });
  };
  
  // Action for clicking the search button
  authCheck = async () => {
    const check = await axios.post("/login/authorize"); 
	this.setState({isAuth: true});
  };

  // Displays the food search, from the food_item object:
    // food_item {food_id,food_name,price, description}
  renderKoreanFoodSearch = () =>
    this.state.koreanFoodSearch.map(food_item => (
      <tr key = {food_item.food_id}>
        <td>{food_item.food_id}</td>
        <td>{food_item.food_name}</td>
        <td>{food_item.price}</td>
        <td>{food_item.description}</td>
      </tr>
    ));

  logout = async () => {
    const _ = await axios.post("/login/logout");
	window.location.href = "/login";
  }
  
  // Styling
  render() {
    return (
      <div className="App">
		{this.state.isAuth &&  <div>
        <form>
          <label>
            <p>Search a Korean Food: </p>
          </label>
          <input
            type="p"
            value={this.state.koreanFoodName}
            onChange={this.onKeyDownKoreanFood}
          />
        </form>
        <button onClick={this.onClickSearch}>Search!</button>
        <center>
          <br />
          <table>
          <tbody>
            <tr>
                <th>Food ID</th>
                <th>Food Name</th>
                <th>Price</th>
                <th>Description</th>
            </tr>
            {this.renderKoreanFoodSearch()}
            </tbody>
          </table>
        </center>
		<button type="button" onClick = {this.logout}> Logout :(</button>
		</div>
		}
      </div>
    );
  }
}

export default koreanFood;
