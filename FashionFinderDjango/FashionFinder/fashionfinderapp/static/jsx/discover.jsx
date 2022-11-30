import './polyfills.jsx';
import {useState} from 'react';
import ReactDOM from 'react-dom';
import React from 'react';
import Navbar from './navbar.jsx';

const ImagePanel = (pieceID) => {

}

// const ControlPanel = (setUserLike) => {
// 	return (
// 		<div>
// 			<button onClick={(e) => alert(e.target.value)}> Like </button>
// 			<button onClick={(e) => alert(e.target.value)}> Dislike </button>
// 		</div>
// 	)
// }


let context = JSON.parse(window._json);
let user_id = JSON.parse(context["user_id"]);

const App = () => {
  return <div>
        <Navbar loggedIn={(user_id !== null)} user_id={user_id}>
			<Discover/>
        </Navbar>

  </div>
  
}

class Discover extends React.Component {
	constructor(props) {
        super(props);
        this.state = {loading: true, item: null};

        // this.handleChange = this.handleChange.bind(this);
        // this.handleSubmit = tgrfwfdhis.handleSubmit.bind(this);
		this.componentDidMount = this.componentDidMount.bind(this);
		this.handleUserVote = this.handleUserVote.bind(this);
    }

	componentDidMount() {

		// TODO: Fetch the uri
		
		// this.setState({source_oid: '6372c3b65b4569cebded16ae', loading: false})
		this.setState({loading: true})
		fetch("/async/discover")
		.then(response => response.json())
		.then(json => this.setState({loading: false, item: json.rec}))
	}

	handleUserVote(event, type) {
		console.log("User voted!")

		if(type == 'like'){
			fetch("/async/discover/like/" + event.target.value)
			.then(response => response.json())
			.then(json => console.log(json))
		}
		fetch("/async/discover/")
		.then(response => response.json())
		.then(json => this.setState({loading: false, item: json.rec}))
	}

	renderRecommendationItem(item) {
		console.log("Rendering recommendation item")
		console.log(item)
		if(item == null || item == undefined){
			return <p> Item can not be properly rendered</p>
		} else {
			return <div 
			className='recommendation-item'>

			
					<img className='recommendation-item-image' 
						src={item.filepath}
						width="200"
						height="200"
						/>
					<div className='recommended-item-image-description-container'>
						{item.descriptor}
					</div>

			</div>

		}
	}


    render() {
		console.log("Render called")
		const {loading, item} = this.state
		console.log(item)
        return (
			<div className='main-page-container'>
				<div className ='voting-item'>
						{loading ? "Loading" : this.renderRecommendationItem(item)}
				</div>
				<div>
					{loading ? <button> Like </button> : <button value={item.id} onClick={(e) => this.handleUserVote(e, 'like')}> Like </button>}
					{loading ? <button> Dislike </button> : <button value={item.id} onClick={(e) => this.handleUserVote(e, 'dislike')}> Dislike </button>}
					{/* <button value={item.id} onClick={(e) => this.handleUserVote(e, 'dislike')}> Dislike </button> */}
				</div>
			</div>
            // <>
                // {/* <SearchStyle /> */}
                // <div className="searchContainer"> 
                    // <form onSubmit={this.handleSubmit}>
                        // <input placeholder="Search for items..." className="searchInput" onChange={this.handleChange} />
                    // </form>
                // </div>
            // </>
        );
    };
}

ReactDOM.render(<App />, document.getElementById('root'));