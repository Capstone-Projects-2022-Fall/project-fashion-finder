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

const WardrobeStyle = () => {
	return <style>
		{`
			.recomendation-comp-items-container {
				margin-top: 20px;
			}
			.recomendation-items-container {
				margin-top: 20px;
			}
			.recommendation-items-container-header {
				min-height: 40px;
				text-align: center;
			}
			.recommendation-comp-items-container-header {
				min-height: 40px;
				text-align: center;
			}
			.recommendation-item {
				margin-top: 5px;
				margin-bottom: 5px;
				border: 1px solid black;
			}
			.recommendation-item-list-container{
				margin-right: 10px;
				margin-top: 10px;
			}

			.wardrobe-and-recommendations-container {
				display: flex;
				justify-content: center;
				border: 1px solid black;
				background: gray;
			}
			.wardobe-and-recommendations {
				display: flex;

			}
			.wardrobe-item{
				display: flex;
			}
			.wardrobe-items-container{
				margin-left: 10%;
				margin-right: 10%;
				max-width: 1000px;
			}
			.wardrobe-item-image{
				border: 1px solid black;
				margin-top: 5px;
				margin-bottom: 5px;
			}
			
			.wardrobe-item-description-container{
				margin-left: 100px;
				margin-top: 10px;
				border: 1px solid black;
				display: inline;
				max-width: 400px;
				min-width: 300px;
			}
			.wardrobe-item-descriptor {
				font-size: 50px;
			}
			.wardrobe-item-owner {
				font-size: 30px;
			}
			.wardrobe-label-header {
				font-weight: bold;
				font-size: 30px;
			}
			.wardrobe-item-hex-codes-header{
				font-weight: bold;
				font-size: 30px;
			}
			.wardrobe-item-label-item {
				font-size: 20px;
			}
			.box {
				float: left;
				height: 20px;
				width: 20px;
				margin-bottom: 15px;
				border: 1px solid black;
				clear: both;
			  }
			  
			.wardrobe-item-hex-list-item {
				display: inline-table;
			}
			
		`}
	</style>
}



const WardrobeItemSelectButtonStyle = () => {
	return <style>
		{`
		.wardrobe-item-select-button {
			min-height: 20px;
			min-width: 100px;
		}
		
		`

		}
	</style> 
}





class Wardrobe extends React.Component {
	constructor(props) {
        super(props);
        this.state = {loading: true, rec_loading: true, rec_comp_loading: true, items: [], rec_items: [], rec_comp_items:[], selected_oid: null};

        // this.handleChange = this.handleChange.bind(this);
        // this.handleSubmit = tgrfwfdhis.handleSubmit.bind(this);
		this.componentDidMount = this.componentDidMount.bind(this);
		this.handleSelectedOIDChange = this.handleSelectedOIDChange.bind(this);
    }

	componentDidMount() {
		fetch("http://localhost:8000/async/wardrobe")
		.then(response => response.json())
		.then(json => this.setState({loading: false, items: json}))
	}

	handleSelectedOIDChange(event) {
		console.log("HANDLE EVENT")
		// console.log(event)
		// console.log(event.target.value)
		console.log("Change!")
		console.log("Rec pieces source OID")
		this.setState({rec_loading: true, rec_items: []})
		
		fetch("http://localhost:8000/async/recommendations/" + event.target.value)
		.then(response => response.json())
		.then(json => this.setState({selected_oid: event.target.value, rec_loading: false, rec_items: json.recs}))

		this.setState({rec_comp_loading: true, rec_comp_items: []})
		fetch("http://localhost:8000/async/recommendations/complementary/" + event.target.value)
		.then(response => response.json())
		.then(json => this.setState({rec_comp_loading: false, rec_comp_items: json.recs}))
		
		
		console.log(this.state.selected_oid)
	}

	renderRecommendationItem(item, index) {
		console.log(item)
		if(item == null || item == undefined){
			return <p> Item can not be properly rendered</p>
		} else {
			return <div 
			className='recommendation-item' key={index}>

			
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
	renderRecommendationList(items) {
		// console.log(items)
		return <div className='recommendation-item-list-container'>
			{items.map((index, item) => this.renderRecommendationItem((item, index)))

			}
		</div>
	}

	renderWardrobeItem(item, index){
		if(item == null || item == undefined){
			return <p> Item can not be properly rendered</p>
		}

		return <div 
		className='wardrobe-item' key={index}>

			<img className='wardrobe-item-image' src={item.filepath}
				width="300"
				height="400"
			/>
			<div className='wardrobe-item-description-container'>
				<p className='wardrobe-item-descriptor'> {item.descriptor}</p>
				<p className='wardrobe-item-owner'> Owner: {item.user_django_name} </p>
				<div className='wardrobe-item-labels'>
					<div className='wardrobe-label-header'>
						Labels
					</div>

					<ul>
						{item.labels.map((item,index) => <li className='wardrobe-item-label-item' key={index}>{item} </li> )}
					</ul>
				</div>
				<div className='wardrobe-item-hex-codes'>
					<p className='wardrobe-item-hex-codes-header'> Detected Colors: </p>
					<ul>
						{item.hex_codes.map((hex_code, index) => 
							
							<li className='wardrobe-item-hex-list-item'key={index}>
								<div className='box' style={{backgroundColor: "#" + hex_code}}> </div>
								{'#' + hex_code}
							</li>
						
						)};
					</ul>
					{/* <ul> */}
					{/* {item.hex_codes.map(item=> <div className='box' style={{background-color: '#348898'}}> </div>)} */}
					{/* </ul> */}
				</div>
				<div className='wardrobe-item-links'>
					<div className='wardrobe-link-see-full-image'>
						<a href={'/static/' + item._id + '.jpg'}> Click here to see the full image</a>
					</div>
				</div>
				<div className='wardrobe-item-select-container'>
					{
					<button  className="wardrobe-item-select-button" onClick={this.handleSelectedOIDChange} value={item._id}>
						Select
					</button>
					}
				</div>
			</div>


		</div>

	}


	renderList(items) {
		// console.log(Object.keys(items))
		// console.log(typeof(items))
		if(items.recs.length == 0){
			return <div> 
				<h2> You don't have any uploaded Images</h2>
						<p> Click "New Upload" above</p>
			</div> 
		} 

		return <ul>
			{items.recs.map((item,index) => this.renderWardrobeItem(item, index))
			
			}

		</ul>
	}

	// renderRecommendedPieces(items){
	// 	if(items.recs.length == 0) {
	// 		return <div> 
	// 		<h2> No Piece selected</h2>
	// 				<p> Click "New Upload" above</p>
	// 		</div> 
	// 	}

	// }


    // handleSubmit(event) {
        // event.preventDefault();
        // window.location.replace('/?search=' + this.state.value)
    // }

    render() {
		console.log("render() re-called")
		const {loading, rec_loading, rec_comp_loading, items, rec_items, rec_comp_items, selected_oid} = this.state

        return (
			<div className='main-page-container'>
				<WardrobeStyle/>
				<div className ='wardobe-and-recommendations'>
					<div className="wardrobe-items-container">
						{loading ? "Loading": this.renderList(items)}
					</div>

					<WardrobeItemSelectButtonStyle/>
					<div className="recomendation-items-container">
						<div className='recommendation-items-container-header'>
							Pieces like this
						</div>
						{selected_oid == null ? "No Piece Selected \t" : this.renderRecommendationList(rec_items)}
					</div>
					<div className="recomendation-comp-items-container">
						<div className='recommendation-comp-items-container-header'>
							Pieces that would go well with this
						</div>
						{selected_oid == null ? "" : this.renderRecommendationList(rec_comp_items)}
					</div>
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

export default Wardrobe