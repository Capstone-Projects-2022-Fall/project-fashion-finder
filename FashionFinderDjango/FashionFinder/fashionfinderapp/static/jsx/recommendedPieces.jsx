import React from "react";


const RecommendationPiecesStyle = () => {
	return <style>
		{`
			.recommendation-container{
				border: 1px, black
			}
		`}
	</style>
}

class RecommendedPieces extends React.Component {
	constructor(props) {
        super(props);
		console.log(props)
        this.state = {loading: true, items: [], source_oid: props.source_oid};

        // this.handleChange = this.handleChange.bind(this);
        // this.handleSubmit = tgrfwfdhis.handleSubmit.bind(this);
		// this.componentDidMount = this.componentDidMount.bind(this);
    }

	componentDidMount() {
		if(this.state.source_oid != null){
			console.log("Rec pieces source OID")
			console.log(this.state.source_oid)
			fetch("http://localhost:8000/async/recommendations/" + this.state.source_oid)
			.then(response => response.json())
			.then(json => this.setState({loading: false, items: json.recs}))
		} else {
			console.log ("RecommendedPieces object mounted with null source_id")
		}
		// Wait for any button click
	}

	renderRecommendationItem(item, index) {
		console.log(item)
		if(item == null || item == undefined){
			return <p> Item can not be properly rendered</p>
		} else {
			return <li key={index}>
				
			<div className='recommendation-item' key={index}>
					<img className='recommendation-item-image' 
						src={item.filepath}
						width="200"
						height="200"
						/>

			</div>
		</li> 

		}
	}

	renderList(items) {
		console.log(items)
		return <ul>
			{items.map((index, item) => this.renderRecommendationItem((item, index)))

			}
		</ul>
	}
	render() {
		const {loading, items, source_id} = this.state
        return (
			<>
			<RecommendationPiecesStyle/>
				<div className="recommendation-container">
					{loading ? "Loading" : this.renderList(items) }
				</div>
			</>

        );
    };
}
export default RecommendedPieces