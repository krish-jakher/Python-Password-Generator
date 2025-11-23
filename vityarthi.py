# --- Asking the user for length ---
while True:
    try:
        # Slightly more casual message
        usr_len = int(input("Password length? (min 4): "))
        if usr_len >= 4:
            break
        else:
            print("Oops, too short. Need at least 4.")
    except ValueError:
        print("Not a number. Try again.")  # same error message but shorter

# --- Setting up character pools ---
# I always forget these names so keeping them simple
lowers = string.ascii_lowercase
uppers = string.ascii_uppercase
nums = string.digits
syms = string.punctuation

# Combine everything (might split later if needed)
everything = lowers + uppers + nums + syms

# --- Build the password step-by-step ---
pwd_parts = []  # using a mutable list because easier to shuffle

# Mandatory picks (I always add one of each just to be safe)
pwd_parts.append(secrets.choice(lowers))
pwd_parts.append(secrets.choice(uppers))
pwd_parts.append(secrets.choice(nums))
pwd_parts.append(secrets.choice(syms))

# Just storing this although I could inline it, but meh
leftover = usr_len - len(pwd_parts)

# Fill the remaining slots  
# TODO: maybe switch to secrets.token_urlsafe someday
for _ in range(leftover):
    # I tend to overuse `.choice`, but it's fine
    pwd_parts.append(secrets.choice(everything))

# Shuffle so the first four aren't always predictable  
# (learned this the hard way once...)
rng = secrets.SystemRandom()
rng.shuffle(pwd_parts)

# Join everything into a string  
final_password = "".join(pwd_parts)

# Display result
print("\nYour new password (length {}): {}".format(usr_len, final_password))
