
import axios from 'axios';

const homeData = {
  slide: {
    caption: 'Sleek your images with our Professional & Creative Image editing agency',
    cover: '',
  },
  card: {
    item1: {
      title: "",
      button_name : "",
      content: "",
      start: "",
      page: "service-fashion",
      link: "contact",
      cover: {
        image: "",
        before: "",
      },
      featureList: {
        Left: [
          
        ],
        Right: [
          
        ],
      },
      viewType: 'left',
    },
    item2: {
      title: "",
      button_name : "",
      content: "",
      start: "",
      page: "service-product",
      link: "contact",
      cover: {
        image: "",
        before: "",
      },
      featureList: {
        Left: [
          
        ],
        Right: [
          
        ],
      },
      viewType: 'right',
    },
    item3: {
      title: "",
      button_name : "",
      page: "service-jewelry",
      content: "",
      start: "",
      link: "contact",
      cover: {
        image: "",
        before: "",
      },
      featureList: {
        Left: [
          
        ],
        Right: [
          
        ],
      },
      viewType: 'left',
    },
	item4: {
		title: "",
    button_name : "",
		page: "service-others",
		content: "",
		start: "",
		link: "contact",
		cover: {
		  image: "",
      before: "",
		},
		featureList: {
		  Left: [
			
		  ],
		  Right: [
			
		  ],
		},
		viewType: 'right',
	  },
  },
};

axios.get('https://app.photoresolve.com/getServices/')
  .then(response => {
		const data = response.data;
		homeData.card.item1.title = data.item1.title;
		homeData.card.item1.button_name = data.item1.button_name;
		homeData.card.item1.content = data.item1.content;
		homeData.card.item1.start = data.item1.start;
		homeData.card.item1.cover.image = data.item1.cover.image;
		homeData.card.item1.featureList.Left = data.item1.featureList.Left;
		homeData.card.item1.featureList.Right = data.item1.featureList.Right;

		homeData.card.item2.title = data.item2.title;
		homeData.card.item2.button_name = data.item2.button_name;
		homeData.card.item2.content = data.item2.content;
		homeData.card.item2.start = data.item2.start;
		homeData.card.item2.cover.image = data.item2.cover.image;
		homeData.card.item2.featureList.Left = data.item2.featureList.Left;
		homeData.card.item2.featureList.Right = data.item2.featureList.Right;

		homeData.card.item3.title = data.item3.title;
		homeData.card.item3.button_name = data.item3.button_name;
		homeData.card.item3.content = data.item3.content;
		homeData.card.item3.start = data.item3.start;
		homeData.card.item3.cover.image = data.item3.cover.image;
		homeData.card.item3.featureList.Left = data.item3.featureList.Left;
		homeData.card.item3.featureList.Right = data.item3.featureList.Right;

		homeData.card.item4.title = data.item4.title;
		homeData.card.item4.button_name = data.item4.button_name;
		homeData.card.item4.content = data.item4.content;
		homeData.card.item4.start = data.item4.start;
		homeData.card.item4.cover.image = data.item4.cover.image;
		homeData.card.item4.featureList.Left = data.item4.featureList.Left;
		homeData.card.item4.featureList.Right = data.item4.featureList.Right;
	})
  .catch(error => {
    console.error(error);
  });

export default homeData;
