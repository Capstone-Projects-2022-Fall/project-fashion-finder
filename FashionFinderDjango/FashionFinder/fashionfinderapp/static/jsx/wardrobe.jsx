import React from "react";
import {useState} from 'react';

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

const CSRFToken = () => {
    return (
        <input type="hidden" name="csrfmiddlewaretoken" value={csrftoken} />
    );
};

// class WardrobeItem extends React.Component {

// }


class Wardrobe extends React.Component {
	constructor(props) {
        super(props);
        this.state = {loading: true, items: []};

        // this.handleChange = this.handleChange.bind(this);
        // this.handleSubmit = tgrfwfdhis.handleSubmit.bind(this);
		this.componentDidMount = this.componentDidMount.bind(this);
    }

	componentDidMount() {
		fetch("http://localhost:8000/async/wardrobe")
		.then(response => response.json())
		.then(json => this.setState({loading: false, items: json}))
	}

	renderList(items) {
		console.log(Object.keys(items))
		console.log(typeof(items))
		if(items.recs.length == 0){
			return <div> 
				<h2> You don't have any uploaded Images</h2>
						<p> Click "New Upload" above</p>
			</div> 
		} 

		return <ul>
			{items.recs.map(item => (
				<li>
					{item.descriptor}
				</li>
			)
			
			)}

		</ul>
	}

    // handleChange(event) {
        // this.setState({value: event.target.value});
    // }

    // handleSubmit(event) {
        // event.preventDefault();
        // window.location.replace('/?search=' + this.state.value)
    // }

    render() {
		const {loading, items} = this.state
        return (
			<>
				<div className="wardrobe-items-container">
					{loading ? "Loading...": this.renderList(this.state.items)}
				</div>
			</>
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

export default Wardrobe