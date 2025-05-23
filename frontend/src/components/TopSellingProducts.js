import react from "react";
import { Link } from "react-router-dom";

const TopSellingProducts = ({products}) =>{
    const topSellingProducts = products
    .sort((a, b) => b.sales - a.sales)
    .slice((0, 10));

    return(
        <>
        <h3> Top Selling Products</h3>
        <div className="row">
            {topSellingProducts.map((product) => (
                <div key={product.id} className="col-md-3"> 
                    <Link to = {`/products/${products.slug}`}>
                    <img src={product.image} alt={product.name}/>
                    <h4>{product.name}</h4>
                    <h4>${product.price}</h4>
                    </Link>
                </div>
            ))}
        </div>
        </>
    );
};

export default TopSellingProducts;