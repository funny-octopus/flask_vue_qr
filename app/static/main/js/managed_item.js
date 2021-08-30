var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        product:null, 
        select_list:['category', 'factory', 'country', 'price_m', 'price_v'],
        factories:null,
        categories:null,
    },
    beforeMount(){
        ident = document.getElementById('ident').value;
        axios.get('/api/item/'+ident)
            .then(response => (this.product = response.data));
        axios.get('/api/factories')
            .then(response => (this.factories = response.data));
        axios.get('/api/categories')
            .then(response => (this.categories = response.data));
    },
    mounted(){
    },

})
