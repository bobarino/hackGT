class ChangeCharityMerchantIdType < ActiveRecord::Migration
  def change
    remove_column :charities, :merchant_id
  end
end
