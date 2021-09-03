var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        product:null, 
        select_list:['category', 'factory', 'country', 'currency', 'price_v'],
        factories:null,
        categories:null,
        items:null,
        changes_flag:false,
    },
    methods:{
        save:function(){
            console.log(this.product);
        },
    },
    created(){
        ident = document.getElementById('ident').value;
        axios.get('/api/item/'+ident)
            .then(response => (this.product = response.data.product));
        axios.get('/api/items')
            .then(response => (this.items = response.data));
    },
    beforeMount(){
    },
    mounted(){
    },

})
