import ftl_nexus

def main():
    config = config.config
    ftl_nexus = FTLNexus(config)
    # Initialize navigation and propulsion systems
    ftl_nexus.navigate("nav_data.csv")
    ftl_nexus.propel("quantum_fluctuations")

if __name__ == "__main__":
    main()
