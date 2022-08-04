
# Usage of http methods

1. As part of KOMASTU dealer, I would like to fetch newly created leads(customers).

# Add one more column to the productenquiry table called sent_to_dealer and its
# data type is Boolean.


SInce you have already implemented GET service , what you do is,
create a list of mobile numbers.

Create a function called set_sent_to_dealer which takes list of
mobile numbers as input and upate the sent_to_dealer to True.


@app.route('/', methods=['GET'])
def home():
    dealercode = request.args.get("dealercode")
    result = session.query(ProductEnquiryForms). \
        filter(ProductEnquiryForms.SentToDealer == 'False',
               ProductEnquiryForms.DealerCode == dealercode).all()
    print(type(result))
    result = [item.__dict__ for item in result]
    mobileno_container = []
    for item in result:
        item.pop('_sa_instance_state')
        mobileno_container.append(item.get('MobileNo'))
    enable_sent_flag(mobileno_container)
    return str(result)


def enable_sent_flag(mobileno_container):
    print("Container {}".format(mobileno_container))
    for mobileno in mobileno_container:
        session.query(ProductEnquiryForms).filter(ProductEnquiryForms.MobileNo == mobileno) \
            .update({"SentToDealer": True})
        session.commit()



2. As part of KOMASTU dealer, I would like to know how many leads I worked for last
    6months.

@app.route('/', methods=['GET'])
def home():
    result = session.query(ProductEnquiryForms). \
        filter(ProductEnquiryForms.CreatedDate >= 2022 - 01 - 01).all()

    result = session.query(ProductEnquiryForms). \
        filter(ProductEnquiryForms.CreatedDate >= 2022 - 01 - 01,
               ProductEnquiryForms.CreatedDate < 2022 - 03 - 01).all()

    result = session.query(ProductEnquiryForms). \
        filter(ProductEnquiryForms.CreatedDate >= 2019 - 01 - 01,
               ProductEnquiryForms.CreatedDate < 2022 - 03 - 01).all()

    return str(result)


http: // 127.0.0.1: 5000 / historic - leads?startdate = 2022 - 01 - 01 & enddate = 2022 - 07 - 26


@app.route('/historic_leads', methods=['GET'])
def get_historic_leads():
    start_date = request.args.get("startdate")
    end_date = request.args.get("enddate")
    result = session.query(ProductEnquiryForms). \
        filter(and_(ProductEnquiryForms.CreatedDate >= start_date,
                    ProductEnquiryForms.CreatedDate <= end_date)).all()
    result = [item.__dict__ for item in result]
    for item in result:
        item.pop('_sa_instance_state')
    return json.dumps(result)


session.query(ProductEnquiryForms).filter(ProductEnquiryForms.SentToDealer == False).all()


@app.route('/get_limited_records1', methods=['GET'])
def get_limited_records1():
    # Limit: How many leads to distribute, offset: Stating point
    result = session.query(ProductEnquiryForms).limit(3).offset(2).all()
    result = [item.__dict__ for item in result]
    for item in result:
        item.pop('_sa_instance_state')
    return str(result)


# 1
# hr - 10000
# 2
# hr - 100000
# 3
# hr - 6786876876886
