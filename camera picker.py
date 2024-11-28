class Camera:
    def __init__(self, name, price, type, features):
        self.name = name
        self.price = price
        self.type = type
        self.features = features

    def __str__(self):
        return f"{self.name} - ${self.price} - {self.type} ({', '.join(self.features)})"

# Camera data array
cameras = [
    Camera("Panasonic Lumix TZ200", 700, "Photography", ["Compact", "Travel zoom", "Versatile"]),
    Camera("Fujifilm GFX 100S", 6000, "Photography", ["Medium format", "High resolution", "Professional"]),
    Camera("Nikon Z fc", 1000, "Photography", ["APS-C", "Retro design", "Compact"]),
    Camera("Canon PowerShot SX740 HS", 400, "Photography", ["Compact", "Superzoom", "Entry-level"]),
    Camera("Panasonic Lumix FZ300", 600, "Photography", ["Bridge camera", "Superzoom", "Weather-sealed"]),
    Camera("Nikon Coolpix W300", 400, "Photography", ["Waterproof", "Compact", "Adventure-friendly"]),
    Camera("Fujifilm X100V", 1400, "Photography", ["Fixed lens", "Compact", "Retro style"]),
    Camera("Olympus Tough TG-6", 500, "Photography", ["Waterproof", "Adventure-friendly", "Compact"]),
    Camera("Canon EOS Rebel T7", 500, "Photography", ["DSLR", "Beginner-friendly", "APS-C"]),
    Camera("Pentax K-70", 700, "Photography", ["DSLR", "Weather-sealed", "APS-C"]),
    Camera("Panasonic Lumix GX85", 800, "Photography", ["Compact", "Micro Four Thirds", "Beginner-friendly"]),
    Camera("Fujifilm X-Pro3", 1800, "Photography", ["APS-C", "Retro style", "Professional"]),
    Camera("Leica M11", 9000, "Photography", ["Full-frame", "Luxury build", "Rangefinder"]),
    Camera("Ricoh GR IIIx", 1000, "Photography", ["Compact", "Fixed lens", "Street photography"]),
    Camera("Nikon D7500", 1000, "Photography", ["DSLR", "APS-C", "Intermediate"]),
    Camera("Sony Alpha a5000", 500, "Photography", ["Mirrorless", "Compact", "Beginner-friendly"]),
    Camera("Panasonic Lumix ZS100", 500, "Photography", ["Compact", "Travel zoom", "Beginner-friendly"]),
    Camera("Nikon Z9", 5500, "Hybrid", ["Full-frame", "Photography", "Videography"]),
    Camera("Fujifilm X-T30 II", 900, "Hybrid", ["APS-C", "Photography", "Videography"]),
    Camera("Sony Alpha a6000", 600, "Photography", ["APS-C", "Compact", "Beginner-friendly"])
]

def get_user_input():
    """
    Prompt user for budget and functionality with improved error handling.
    
    Returns:
    tuple: (budget, functionality) or (None, None) if input is invalid
    """
    while True:
        try:
            budget = input("Enter your budget (in USD): ").strip()
            
            # Check if budget is a valid number
            if not budget.isdigit():
                print("Error: Budget must be a positive number.")
                continue
            
            budget = int(budget)
            
            if budget <= 0:
                print("Error: Budget must be greater than zero.")
                continue
            
            # Get functionality with input validation
            valid_functionalities = ["photography", "videography", "hybrid", "vlogging"]
            print("\nAvailable Functionalities:")
            for func in valid_functionalities:
                print(f"- {func.capitalize()}")
            
            functionality = input("Enter functionality: ").strip().lower()
            
            if functionality not in valid_functionalities:
                print(f"Error: Invalid functionality. Choose from: {', '.join(valid_functionalities)}")
                continue
            
            return budget, functionality
        
        except ValueError:
            print("Error: Invalid input. Please try again.")
        
        except KeyboardInterrupt:
            print("\nSearch cancelled.")
            return None, None

def recommend_camera(budget, functionality):
    """
    Find cameras matching budget and functionality.
    
    Args:
    budget (int): Maximum price
    functionality (str): Desired camera type
    
    Returns:
    list: Matching cameras
    """
    recommendations = [
        camera for camera in cameras
        if camera.price <= budget and functionality in camera.type.lower()
    ]
    
    # Sort recommendations by price (ascending)
    recommendations.sort(key=lambda x: x.price)
    
    return recommendations

def display_recommendations(recommendations):
    """
    Display camera recommendations with additional details.
    
    Args:
    recommendations (list): List of recommended cameras
    """
    if recommendations:
        print("\n--- Recommended Cameras ---")
        for i, camera in enumerate(recommendations, 1):
            print(f"\n{i}. {camera}")
            print("   Features Highlight:")
            for feature in camera.features:
                print(f"   - {feature}")
    else:
        print("\nNo cameras found matching your criteria. Try adjusting your budget or functionality.")

def main():
    print("🎥 Welcome to the Advanced Camera Finder! 📷")
    
    # Main search loop
    while True:
        budget, functionality = get_user_input()
        
        if budget is None or functionality is None:
            break
        
        recommendations = recommend_camera(budget, functionality)
        display_recommendations(recommendations)
        
        # Ask if user wants to search again
        again = input("\nWould you like to search again? (yes/no): ").strip().lower()
        if again != 'yes':
            break
    
    print("\nThank you for using the Camera Finder! 👋")

if __name__ == "__main__":
    main()
