var appp = new Vue({
    el:'#app',
    delimiters:['[[',']]'],
    data:{
        resp:'',
        items:[],
        link_back:false,
        cur_cat:'category',
        cat_id: 1,
        filt:'',
        factory:'all',
        collection:'all',
        provider:'all',
	factories: [],
	collections: [],
	providers: [],
        size:24,
        page_number:0,

    },
    watch:{
        resp: function(new_resp, old_resp){
	    console.log(new_resp.items);
	    this.items = new_resp.items;
	    this.factories = new_resp.factories.filter((v, i, a) => a.indexOf(v) === i).sort();
	    this.collections = new_resp.collections.filter((v, i, a) => a.indexOf(v) === i).sort();
	    this.providers = new_resp.providers.filter((v, i, a) => a.indexOf(v) === i).sort();
	},
    },
    computed:{
        filtred_items:function(){
            this.page_number = 0;
            var f = this.filt.toLowerCase();
            return this.items.filter(function(elem){
                if(f==='')return true;
                else return elem.name.toLowerCase().indexOf(f) > -1 || elem.article.toLowerCase().indexOf(f) > -1;
            });
        },
        page_count:function(){
            var l = this.filtred_items.length,
                s = this.size;
            return Math.ceil(l/s);
        },
        paginated_data:function(){
            const start = this.page_number * this.size,
                  end = start + this.size;
            return this.filtred_items.slice(start, end);
        },
        factories_:function(){
	    var ff = this.items.map(item => item.factory);
	    var f = ff.filter((v, i, a) => a.indexOf(v) === i);
            return f.sort()
        },
        collections_:function(){
            var cc = this.items.map(item => item.collection);
            var c = cc.filter((v, i, a) => a.indexOf(v) === i);
            return c.sort();
        },
	providers_:function(){
            var pp = this.items.map(item => item.provider);
            var p = pp.filter((v, i, a) => a.indexOf(v) === i);
            return p.sort();
	},

    },
    methods:{
        get_items:function(id_ = this.cat_id){
		console.log("GET")
            this.items=[];
            this.cur_cat = 'product';
            this.link_back = true;
            this.page_number = 0;
	    factory_ = this.factory === 'all' ? "" : this.factory;
	    collection_ = this.collection === 'all' ? "" : this.collection;
	    provider_ = this.provider === 'all' ? "" : this.provider;
            axios.get('/api/products/'+id_, { params: {factory: factory_, collection: collection_, provider: provider_} })
                    .then(response => this.resp = response.data);

        },
        change_cur_cat:function(){
            this.items=[];
            this.cur_cat = 'category';
            this.link_back = false;
            this.filt = '';
            this.page_number = 0;
            this.factory = 'all';
            this.collection = 'all';
            this.provider = 'all';
            axios.get('/api/category/')
                .then(response => this.items = response.data.items);
        },
        redirect_to_item:function(product_id){
            window.location.replace('/item/' + product_id);
        },
        next_page:function(){
            this.page_number++;
        },
        prev_page:function(){
            this.page_number--;
        },
    },
    beforeCreate(){
        axios.get('/api/category/')
            .then(response => this.items = response.data.items);
    },


})
