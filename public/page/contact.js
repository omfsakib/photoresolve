import axios from "axios";

export default {
    data() {
        return {
            caption: "",
            phone: "",
            email: "",
            address: "",
        };
    },

    mounted() {
        axios.get("https://app.photoresolve.com/getContact/")
            .then(response => {
                const data = response.data;
                this.caption = data.caption;
                this.phone = data.phone || "";
                this.email = data.email;
                this.address = data.address || "";
            })
            .catch(error => console.log(error));
    },
};

