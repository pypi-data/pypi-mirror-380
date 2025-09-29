def moreau_decomp(proximal):
    return lambda x: x - proximal(x)



if __name__ == "__main__":
    main()
