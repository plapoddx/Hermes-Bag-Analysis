def split_hermes_data(df):
    # Create a copy of the DataFrame to avoid modifying the original
    processed_df = df.copy()
    
    # 1. Add parentheses to make the patterns into capture groups
    hermes_leather = r'(Togo|Epsom|Teddy|Swift|swift|Mysore Chèvre|Touch|Chèvre|Chèvre Chamkila|Chamkila|Box|Chevre|Barenia|Clemence|Evercolor|Evergrain|Taurillon Maurice|Taurillon Novillo|Vache Hunter|Veau Madame|Tadelakt|Togo Butler|Sombrero|Grizzly|Doblis|Buffalo|Vachette Crispe|Teddy Shearling)'
    hermes_exotic_skin = r'(Alligator Mississippiensis|Satine Boreal Alligator|Matte Gator|Matte Alligator|Prosus|Porosus|Porosus Crocodile|Alligator Matte|Crocodile Niloticus|Niloticus Croc|Croc|Crocodile Porosus|Crocodile Himalaya|Lizard|Lizard Ombre|Ostrich|Python|Barenia Alligator)'
    hermes_stitching = r'(Retourne|Sellier)'
    hermes_limited_edition = r'(Casaque|Chamikla|Studded|Chamika|Étoilée|Touch|Teddy|Himalaya|Tri-Color|Canvas|Suede|Verso|Picnic|Côte à Côte|Sellier Aizome|Ombre|Mirror|Cargo|In & Out|Faubourg|Shadow|Fringe|Club|Clouté|Cavalcadour|Rock|Quadrille|Mosaic|Tressage|Graphite)'
    
    # 2. Split Bag Type and Bag Size
    processed_df[['Bag_Type', 'Bag_Size']] = processed_df['Bag_Type'].str.split(' ', expand=True)
    
    # 3. Extract materials and styles with error handling
    try:
        processed_df['Leather'] = processed_df['Material_Style'].str.extract(hermes_leather)
        processed_df['Exotic_Skin'] = processed_df['Material_Style'].str.extract(hermes_exotic_skin)
        processed_df['Stitching'] = processed_df['Material_Style'].str.extract(hermes_stitching)
        processed_df['Limited_Edition'] = processed_df['Material_Style'].str.extract(hermes_limited_edition)

    #4. Filling Bag "Constance" with Sellier Stitching
        processed_df.loc[processed_df['Bag_Type'].str.contains('Constance', na=False), 'Stitching'] = processed_df \
                    .loc[processed_df['Bag_Type'].str.contains('Constance', na=False), 'Stitching'] \
                    .fillna('Sellier')    
    
    #5. Filling Bag "Lindy" with Retourne Stitching
        processed_df.loc[processed_df['Bag_Type'].str.contains('Lindy', na=False), 'Stitching'] = processed_df \
                    .loc[processed_df['Bag_Type'].str.contains('Lindy', na=False), 'Stitching'] \
                    .fillna('Retourne')          
         
    #6. Filling Bag "Evelyne" with Retourne Stitching
        processed_df.loc[processed_df['Bag_Type'].str.contains('Evelyne', na=False), 'Stitching'] = processed_df \
                    .loc[processed_df['Bag_Type'].str.contains('Evelyne', na=False), 'Stitching'] \
                    .fillna('Retourne')       

    #7. Filling Bag "Mini Kelly 7.5" with Sellier Stitching
        processed_df.loc[processed_df['Bag_Size'].str.contains('7.5', na=False), 'Stitching'] = processed_df \
                    .loc[processed_df['Bag_Size'].str.contains('7.5', na=False), 'Stitching'] \
                    .fillna('Sellier')    
    
    #8. Filling Bag "Kelly" with NaN Stitching with Sellier Stitching
        processed_df.loc[processed_df['Bag_Type'].str.contains('Kelly', na=True), 'Stitching'] = processed_df \
                    .loc[processed_df['Bag_Type'].str.contains('Kelly', na=True), 'Stitching'] \
                    .fillna('Sellier')    

    #8. Filling Bag "Birkin" with NaN Stitching with Retourne Stitching
        processed_df.loc[processed_df['Bag_Type'].str.contains('Birkin', na=True), 'Stitching'] = processed_df \
                    .loc[processed_df['Bag_Type'].str.contains('Birkin', na=True), 'Stitching'] \
                    .fillna('Retourne')    

    #9. Filling Bag "HAC" with NaN Stitching with Retourne Stitching
        processed_df.loc[processed_df['Bag_Type'].str.contains('HAC', na=True), 'Stitching'] = processed_df \
                    .loc[processed_df['Bag_Type'].str.contains('HAC', na=True), 'Stitching'] \
                    .fillna('Retourne')    
              
    # 10. Fill NaN values
        processed_df['Leather'] = processed_df['Leather'].fillna('Exotic')
        processed_df['Exotic_Skin'] = processed_df['Exotic_Skin'].fillna('Regular Leather')
        #processed_df['Stitching'] = processed_df['Stitching'].fillna('')
        processed_df['Limited_Edition'] = processed_df['Limited_Edition'].fillna('Regular')
        
    except Exception as e:
        print(f"Error processing materials: {e}")
    
    return processed_df