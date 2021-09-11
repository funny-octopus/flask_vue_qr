var appp = new Vue({
    el:'#app',
    delimiters:['[[',']]'],
    data:{
        items:null,
        link_back:false,
        cur_cat:'category',

    },
    methods:{
        get_items:function(id){
            this.cur_cat = 'product';
            this.link_back = true;
            axios.get('/api/products/'+id)
                    .then(response => this.items = response.data.items);
        },
        change_cur_cat:function(){
            this.cur_cat = 'category';
            this.link_back = false;
            axios.get('/api/category/')
                .then(response => this.items = response.data.items);
        },
        redirect_to_item:function(product_id){
            console.log('сработала функция');
            window.location.replace('/item/' + product_id);
        },
    },
    mounted(){
        axios.get('/api/category/')
            .then(response => this.items = response.data.items);
    },


})
