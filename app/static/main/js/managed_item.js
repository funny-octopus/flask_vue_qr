var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        id:null,
        product:null, 
        resp:null,
        select_list:['category', 'factory', 'country', 'currency', 'price_v'],
        factories:null,
        categories:null,
        items:null,
        changes_flag:false,
    },
    methods:{
        save:function(){
            console.log(this.resp.product);
            this.changes_flag=false;
        },
    },
    created(){
        ident = document.getElementById('ident').value;
        axios.get('/api/item/'+ident)
        // .then(response => (this.product = response.data.product;this.id = response.data.id;));
            .then(response => (this.resp = response.data));
        axios.get('/api/items')
            .then(response => (this.items = response.data));
    },
    beforeMount(){
    },
    mounted(){
    },

})
