import sys
import os

# Add project root to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.main import app, db, Perfume # Import app, db, and Perfume model

perfumes_to_add = [
    {
        "name": "Born in Roma Intense (eau de parfum)",
        "brand": "Valentino",
        "category": "Diseñador",
        "gender": "Hombre",
        "image1_filename": "valentino_born_in_roma_intense.png",
        "price_3ml": 6.50,
        "price_5ml": 9.25,
        "price_10ml": 16.99,
        "availability": "Disponible"
    },
    {
        "name": "Le Beau Le Parfum (eau de parfum)",
        "brand": "Jean Paul Gaultier",
        "category": "Diseñador",
        "gender": "Hombre",
        "image1_filename": "jpg_le_beau_le_parfum.png",
        "price_3ml": 6.25,
        "price_5ml": 8.50,
        "price_10ml": 14.99,
        "availability": "Disponible"
    },
    {
        "name": "Le Male Le Parfum (eau de parfum intense)",
        "brand": "Jean Paul Gaultier",
        "category": "Diseñador",
        "gender": "Hombre",
        "image1_filename": "jpg_le_male_le_parfum_intense.png",
        "price_3ml": 5.25,
        "price_5ml": 7.99,
        "price_10ml": 14.99,
        "availability": "Disponible"
    },
    {
        "name": "The Most Wanted (eau de parfum intense)",
        "brand": "Azzaro",
        "category": "Diseñador",
        "gender": "Hombre",
        "image1_filename": "azzaro_the_most_wanted_edp_intense.png",
        "price_3ml": 5.75,
        "price_5ml": 8.50,
        "price_10ml": 14.50,
        "availability": "Disponible"
    },
    {
        "name": "Legend Spirit (eau de toilette)",
        "brand": "Montblanc",
        "category": "Diseñador",
        "gender": "Hombre",
        "image1_filename": "montblanc_legend_spirit_edt.png",
        "price_3ml": 3.50,
        "price_5ml": 4.50,
        "price_10ml": 7.99,
        "availability": "Disponible"
    },
    {
        "name": "Eros EDP (eau de parfum)",
        "brand": "Versace",
        "category": "Diseñador",
        "gender": "Hombre",
        "image1_filename": "versace_eros_edp.png",
        "price_3ml": 5.25,
        "price_5ml": 7.50,
        "price_10ml": 13.99,
        "availability": "Disponible"
    },
    {
        "name": "Khamrah Qahwa (eau de parfum)",
        "brand": "Lattafa",
        "category": "Diseñador", # As per user instruction for image 8
        "gender": "Unisex",
        "image1_filename": "lattafa_khamrah_qahwa.png",
        "price_3ml": 3.50,
        "price_5ml": 4.50,
        "price_10ml": 7.99,
        "availability": "Disponible"
    },
    {
        "name": "Khamrah (eau de parfum)",
        "brand": "Lattafa",
        "category": "Árabe",
        "gender": "Unisex",
        "image1_filename": "lattafa_khamrah.png",
        "price_3ml": 3.50,
        "price_5ml": 4.50,
        "price_10ml": 7.99,
        "availability": "Disponible"
    },
    {
        "name": "Amber Oud Gold Edition (eau de parfum)",
        "brand": "Al Haramain",
        "category": "Árabe",
        "gender": "Unisex",
        "image1_filename": "alharamain_amber_oud_gold.png",
        "price_3ml": 4.50,
        "price_5ml": 6.25,
        "price_10ml": 10.99,
        "availability": "Disponible"
    },
    {
        "name": "Asad (eau de parfum)",
        "brand": "Lattafa",
        "category": "Árabe",
        "gender": "Hombre",
        "image1_filename": "lattafa_asad.png",
        "price_3ml": 3.50,
        "price_5ml": 4.99,
        "price_10ml": 8.99,
        "availability": "Disponible"
    },
    {
        "name": "Asad Bourbon (eau de parfum)",
        "brand": "Lattafa",
        "category": "Árabe",
        "gender": "Hombre",
        "image1_filename": "lattafa_asad_bourbon.png",
        "price_3ml": 3.99,
        "price_5ml": 5.50,
        "price_10ml": 8.99,
        "availability": "Disponible"
    },
    {
        "name": "Yara (eau de parfum)",
        "brand": "Lattafa",
        "category": "Árabe",
        "gender": "Mujer",
        "image1_filename": "lattafa_yara.png",
        "price_3ml": 3.50,
        "price_5ml": 4.99,
        "price_10ml": 8.50,
        "availability": "Disponible"
    },
    {
        "name": "Yara Candy (eau de parfum)",
        "brand": "Lattafa",
        "category": "Árabe",
        "gender": "Mujer", # As per user instruction for image 14
        "image1_filename": "lattafa_yara_candy.png",
        "price_3ml": 3.50,
        "price_5ml": 4.99,
        "price_10ml": 8.50,
        "availability": "Disponible"
    },
    {
        "name": "Club de Nuit Intense Man (eau de parfum)",
        "brand": "Armaf",
        "category": "Árabe",
        "gender": "Hombre", # Corrected based on name, despite user saying Mujer for 15
        "image1_filename": "armaf_cdnim.png",
        "price_3ml": 3.50,
        "price_5ml": 4.99,
        "price_10ml": 8.50,
        "availability": "Disponible"
    },
    {
        "name": "Amber Oud Tobacco Edition (eau de parfum)",
        "brand": "Al Haramain",
        "category": "Árabe",
        "gender": "Unisex",
        "image1_filename": "alharamain_amber_oud_tobacco.png",
        "price_3ml": 4.50,
        "price_5ml": 6.25,
        "price_10ml": 10.99,
        "availability": "Disponible"
    }
]

def add_perfumes():
    with app.app_context():
        existing_names = {p.name for p in Perfume.query.all()}
        added_count = 0
        skipped_count = 0
        for data in perfumes_to_add:
            if data["name"] in existing_names:
                print(f"Skipping existing perfume: {data['name']}")
                skipped_count += 1
                continue
            try:
                perfume = Perfume(**data)
                db.session.add(perfume)
                added_count += 1
                print(f"Adding perfume: {data['name']}")
            except Exception as e:
                print(f"Error adding perfume {data['name']}: {e}")
                db.session.rollback()
                # Optionally break or continue on error
                break # Stop if one fails

        if added_count > 0:
            try:
                db.session.commit()
                print(f"Successfully added {added_count} perfumes.")
            except Exception as e:
                print(f"Error committing changes: {e}")
                db.session.rollback()
        else:
            print("No new perfumes were added.")
        
        if skipped_count > 0:
            print(f"Skipped {skipped_count} existing perfumes.")

if __name__ == "__main__":
    add_perfumes()

